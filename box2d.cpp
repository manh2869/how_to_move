#include <SFML/Graphics.hpp>
#include <box2d/box2d.h>
#include <iostream>

using namespace sf;

int main()
{
    RenderWindow window(
        VideoMode({1000, 700}),
        "SFML + Box2D"
    );

    window.setFramerateLimit(60);

    // 50 pixel = 1 met trong Box2D
    const float SCALE = 50.0f;

    // 1. Tao the gioi vat ly
    b2Vec2 gravity(0.0f, 9.8f);
    b2World world(gravity);

    // 2. Tao mat dat
    b2BodyDef groundDef;
    groundDef.position.Set(10.0f, 12.6f);

    b2Body* ground = world.CreateBody(&groundDef);

    b2PolygonShape groundShape;
    groundShape.SetAsBox(10.0f, 0.4f);

    ground->CreateFixture(&groundShape, 0.0f);

    // 3. Tao qua bong dong
    b2BodyDef ballDef;
    ballDef.type = b2_dynamicBody;
    ballDef.position.Set(10.0f, 2.0f);

    b2Body* ball = world.CreateBody(&ballDef);

    b2CircleShape ballShape;
    ballShape.m_radius = 0.35f;

    b2FixtureDef ballFixture;
    ballFixture.shape = &ballShape;
    ballFixture.density = 1.0f;
    ballFixture.friction = 0.4f;
    ballFixture.restitution = 0.5f;

    ball->CreateFixture(&ballFixture);

    // 4. Hinh ve SFML
    CircleShape circle(0.35f * SCALE);
    circle.setOrigin({
        0.35f * SCALE,
        0.35f * SCALE
    });
    circle.setFillColor(Color::Blue);

    RectangleShape floor({
        1000.0f,
        40.0f
    });
    floor.setPosition({0.0f, 630.0f});
    floor.setFillColor(Color(80, 80, 80));

    // 5. Vong lap game
    Clock clock;
    float accumulator = 0.0f;
    const float timeStep = 1.0f / 60.0f;

    while (window.isOpen())
    {
        while (const auto event = window.pollEvent())
        {
            if (event->is<Event::Closed>())
                window.close();
        }

        float frameTime = clock.restart().asSeconds();
        if (frameTime > 0.25f)
            frameTime = 0.25f;

        accumulator += frameTime;

        while (accumulator >= timeStep)
        {
            world.Step(timeStep, 8, 3);
            accumulator -= timeStep;
        }

        // Lay vi tri tu Box2D
        b2Vec2 p = ball->GetPosition();

        // Doi met thanh pixel
        circle.setPosition({
            p.x * SCALE,
            p.y * SCALE
        });

        window.clear(Color::White);
        window.draw(floor);
        window.draw(circle);
        window.display();
    }

    return 0;
}
