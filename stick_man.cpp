#include <SFML/Graphics.hpp>
#include <iostream>
using namespace std;
using namespace sf;

struct Head
{
    CircleShape shape;

    Head(Vector2f pos, Color color, float radius)
    {
        shape.setRadius(radius);
        shape.setPosition(pos);
        shape.setFillColor(color);
    }
};
struct Chest
{
    RectangleShape shape;

    Chest(Vector2f pos, Color color, Vector2f size)
    {
        shape.setPosition(pos);
        shape.setFillColor(color);
        shape.setSize(size);
    }
};

struct Arm
{
    RectangleShape shape;

    Arm(Vector2f pos, Color color, Vector2f size)
    {
        shape.setPosition(pos);
        shape.setFillColor(color);
        shape.setSize(size);
    }
};

struct Leg
{
    RectangleShape shape;

    Leg(Vector2f pos, Color color, Vector2f size)
    {
        shape.setPosition(pos);
        shape.setFillColor(color);
        shape.setSize(size);
    }
};
struct body
{
    Head head;
    Chest chest;
    Arm leftArm;
    Arm rightArm;
    Leg leftLeg;
    Leg rightLeg;

    body()
        : head({390, 100}, Color::Yellow, 30),
          chest({385, 160}, Color::Blue, {40, 80}),
          leftArm({355, 165}, Color::Red, {25, 70}),
          rightArm({430, 165}, Color::Red, {25, 70}),
          leftLeg({385, 245}, Color::Green, {15, 70}),
          rightLeg({410, 245}, Color::Green, {15, 70})
    {
    }

    void draw(RenderWindow &window)
    {
        window.draw(head.shape);
        window.draw(chest.shape);
        window.draw(leftArm.shape);
        window.draw(rightArm.shape);
        window.draw(leftLeg.shape);
        window.draw(rightLeg.shape);
    }
};

int main()
{
    RenderWindow window(VideoMode({1000, 700}), "stick man");
    Clock clock;
    window.setFramerateLimit(120);
    body man;
    while (window.isOpen())
    {
        while (const auto event = window.pollEvent())
        {
            if (event->is<Event::Closed>())
                window.close();
        }
        Vector2i mouse = Mouse::getPosition(window);
        // man.head.setPosition({float(mouse.x) - man.head.getRadius(), float(mouse.y) - man.head.getRadius()});
        float dt = clock.restart().asSeconds();
        window.clear(Color::White);
        man.draw(window);
        // window.draw(man.head);
        window.display();
    };
}
