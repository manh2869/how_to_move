#include <SFML/Graphics.hpp>
#include <cmath>
#include <vector>
using namespace std;
using namespace sf;

const float GRAVITY = 980.f;
const float L1 = 150.f; // độ dài dây 1
const float L2 = 150.f; // độ dài dây 2
const float R1 = 18.f;
const float R2 = 18.f;

struct Bob
{
    Vector2f pos, prev;
};

float length(Vector2f v) { return sqrt(v.x * v.x + v.y * v.y); }

void drawRod(RenderWindow &window, Vector2f a, Vector2f b)
{
    Vector2f d = b - a;
    RectangleShape r({length(d), 4.f});
    r.setOrigin({0.f, 2.f});
    r.setPosition(a);
    r.setRotation(radians(atan2(d.y, d.x)));
    r.setFillColor(Color::Red);
    window.draw(r);
}

void drawBall(RenderWindow &window, Vector2f p, float radius, Color color)
{
    CircleShape c(radius);
    c.setOrigin({radius, radius});
    c.setPosition(p);
    c.setFillColor(color);
    window.draw(c);
}

int main()
{
    RenderWindow window(VideoMode({1000, 700}), "double pendulum");
    window.setFramerateLimit(120);
    Clock clock;

    Vector2f pivot = {500.f, 200.f};
    Bob b1, b2;

    auto reset = [&]()
    {
        // thả từ vị trí nằm ngang cho dễ thấy chuyển động hỗn loạn
        b1.pos = b1.prev = pivot + Vector2f(L1, 0.f);
        b2.pos = b2.prev = b1.pos + Vector2f(L2, 0.f);
    };
    reset();

    vector<Vertex> trail; // vệt đường đi của B2
    bool dragging = false;

    while (window.isOpen())
    {
        while (const auto event = window.pollEvent())
        {
            if (event->is<Event::Closed>())
                window.close();
            if (const auto *e = event->getIf<Event::MouseButtonPressed>())
                if (e->button == Mouse::Button::Left)
                    dragging = true;
            if (const auto *e = event->getIf<Event::MouseButtonReleased>())
                if (e->button == Mouse::Button::Left)
                    dragging = false;
            if (const auto *e = event->getIf<Event::KeyPressed>())
                if (e->code == Keyboard::Key::R)
                {
                    pivot = {500.f, 200.f};
                    reset();
                    trail.clear();
                }
        }

        float frameTime = min(clock.restart().asSeconds(), 0.033f);
        Vector2i mi = Mouse::getPosition(window);

        const int substeps = 8;
        float dt = frameTime / substeps;
        for (int s = 0; s < substeps; s++)
        {
            // giữ chuột trái thì điểm treo đi theo chuột
            if (dragging)
                pivot = Vector2f(float(mi.x), float(mi.y));

            // 1. trọng lực + quán tính (Verlet)
            for (Bob *b : {&b1, &b2})
            {
                Vector2f vel = b->pos - b->prev;
                b->prev = b->pos;
                b->pos += vel + Vector2f(0.f, GRAVITY * dt * dt);
            }

            // 2. ràng buộc độ dài dây
            for (int i = 0; i < 10; i++)
            {
                // dây 1: P ghim cứng, chỉ B1 dịch (hết phần sai)
                Vector2f d = b1.pos - pivot;
                float dist = length(d);
                if (dist > 0.0001f)
                    b1.pos = pivot + d * (L1 / dist);

                // dây 2: B1 và B2 mỗi bên một nửa
                d = b2.pos - b1.pos;
                dist = length(d);
                if (dist > 0.0001f)
                {
                    float diff = (dist - L2) / dist;
                    b1.pos += d * (0.5f * diff);
                    b2.pos -= d * (0.5f * diff);
                }
            }
        }

        // lưu vệt
        trail.push_back(Vertex{b2.pos, Color(0, 120, 255)});
        if (trail.size() > 400)
            trail.erase(trail.begin());

        window.clear(Color::White);
        if (trail.size() > 1)
            window.draw(trail.data(), trail.size(), PrimitiveType::LineStrip);
        drawRod(window, pivot, b1.pos);
        drawRod(window, b1.pos, b2.pos);
        drawBall(window, pivot, 5.f, Color::Black);
        drawBall(window, b1.pos, R1, Color::Green);
        drawBall(window, b2.pos, R2, Color::Green);
        window.display();
    }
}