#include "raylib.h"
#include <iostream>
using namespace std;

int main()
{
    InitWindow(900, 900, "Stickman");
    SetTargetFPS(120);

    Vector2 pos = {300, 300};

    float gravity = 980.0f;
    float speed = 200.0f;
    float elastic = 0.75f;
    float velocityY = 0.0f;

    float radius = 30.0f;
    float groundY = 700.0f;

    while (!WindowShouldClose())
    {
        float dt = GetFrameTime();
        if (IsKeyDown(KEY_RIGHT))
            pos.x += speed * dt;
        if (IsKeyDown(KEY_LEFT))
            pos.x -= speed * dt;

        velocityY += gravity * dt;
        cout<<velocityY<<endl;
        pos.y += velocityY * dt;

        if (pos.y + radius >= groundY)
        {
            pos.y = groundY - radius;

            if (velocityY > 0)
                velocityY = -velocityY * elastic;

        }

        if (IsKeyDown(KEY_UP))
            pos.y -= speed * dt;
        if (IsKeyDown(KEY_DOWN))
            pos.y += speed * dt;

        BeginDrawing();
        ClearBackground(RAYWHITE);

        DrawRectangle(0, (int)groundY, 900, 30, BLUE);
        DrawCircleV(pos, radius, BLACK);

        DrawText(TextFormat("FPS: %i", GetFPS()),
                 10, 10, 20, BLACK);

        EndDrawing();
    }

    CloseWindow();
    return 0;
}
