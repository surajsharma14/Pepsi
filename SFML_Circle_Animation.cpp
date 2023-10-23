#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>

int main() {
    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Animation");

    sf::CircleShape shape(50); // Create a circle shape with radius 50
    shape.setFillColor(sf::Color::Green); // Set circle color to green

    // Animation loop
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Update animation logic here (e.g., move the shape)
        shape.move(0.1f, 0); // Move the shape to the right

        window.clear(); // Clear the window
        window.draw(shape); // Draw the shape
        window.display(); // Display the rendered frame
    }

    return 0;
}
