#include <SFML/Graphics.hpp>
#include <iostream>
using namespace std;
using namespace sf;

struct body
{
    CircleShape head;
    body(Vector2f pos, Color color, float radius)
    {
        head.setPosition(pos);
        head.setFillColor(color);
        head.setRadius(radius);
    }
};
int main()
{
    RenderWindow window(VideoMode({1000, 700}), "stick man");
    Clock clock;
    window.setFramerateLimit(120);
    body man({400, 400}, Color ::Green, 40);
    while (window.isOpen())
    {
        while (const auto event = window.pollEvent())
        {
            if (event->is<Event::Closed>())
                window.close();
        }
        Vector2i mouse = Mouse::getPosition(window);
        man.head.setPosition({float(mouse.x) - man.head.getRadius(), float(mouse.y) - man.head.getRadius()});
        float dt = clock.restart().asSeconds();
        window.clear(Color::White);
        window.draw(man.head);
        window.display();
    };
}
