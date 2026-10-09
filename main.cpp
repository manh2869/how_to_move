
#include "raylib.h"
#include "raymath.h"

int main()
{
    const int screenWidth = 1280;
    const int screenHeight = 720;

    InitWindow(screenWidth, screenHeight, "3D Sphere - Free Camera");
    SetTargetFPS(120);
    DisableCursor();

    Camera3D camera = {0};
    camera.position = {4.0f, 3.0f, 6.0f};
    camera.target = {0.0f, 0.0f, 0.0f};
    camera.up = {0.0f, 1.0f, 0.0f};
    camera.fovy = 60.0f;
    camera.projection = CAMERA_PERSPECTIVE;

    float moveSpeed = 3.0f;

    while (!WindowShouldClose())
    {
        float dt = GetFrameTime();
        UpdateCamera(&camera, CAMERA_FREE);
        Vector3 forward = Vector3Subtract(
            camera.target, camera.position
        );
        forward.y = 0.0f;
        forward = Vector3Normalize(forward);
        Vector3 right = Vector3Normalize(
            Vector3CrossProduct(forward, camera.up)
        );
        if (IsKeyDown(KEY_W))
            camera.position = Vector3Add(
                camera.position,
                Vector3Scale(forward, moveSpeed * dt)
            );
        if (IsKeyDown(KEY_S))
            camera.position = Vector3Subtract(
                camera.position,
                Vector3Scale(forward, moveSpeed * dt)
            );
        if (IsKeyDown(KEY_D))
            camera.position = Vector3Add(
                camera.position,
                Vector3Scale(right, moveSpeed * dt)
            );
        if (IsKeyDown(KEY_A))
            camera.position = Vector3Subtract(
                camera.position,
                Vector3Scale(right, moveSpeed * dt)
            );
        if (IsKeyDown(KEY_SPACE))
            camera.position.y += moveSpeed * dt;
        if (IsKeyDown(KEY_LEFT_SHIFT))
            camera.position.y -= moveSpeed * dt;
        Vector3 direction = Vector3Subtract(
            camera.target, camera.position
        );
        camera.target = Vector3Add(
            camera.position, direction
        );

        BeginDrawing();
        ClearBackground(RAYWHITE);

        BeginMode3D(camera);

        DrawPlane(
            {0.0f, -1.0f, 0.0f},
            {100.0f, 0.1f},
            LIGHTGRAY
        );

        DrawGrid(20, 1.0f);

        // DrawSphere({0.0f, 1.0f, 0.0f}, 1.0f, RED);
        DrawSphereWires(
            {0.0f, 1.0f, 0.0f}, 1.0f, 16, 16, MAROON
        );
        DrawLine3D(
            {0, 0, 0}, {3, 0, 0}, RED
        );
        DrawLine3D(
            {0, 0, 0}, {0, 3, 0}, GREEN
        );
        DrawLine3D(
            {0, 0, 0}, {0, 0, 3}, BLUE
        );
        EndMode3D();
        DrawFPS(20, 80);
        EndDrawing();
    }
    CloseWindow();
    return 0;
}