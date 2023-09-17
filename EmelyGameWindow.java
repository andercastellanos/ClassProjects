import java.awt.Dimension;
import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.HeadlessException;
import java.awt.GridLayout;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

public class GameWindow extends JFrame {

    // Constructor for the GameWindow class
    public GameWindow() throws HeadlessException {
        super("Poker"); // Set the title of the JFrame
        setDefaultCloseOperation(EXIT_ON_CLOSE); // Set the default close operation to exit the application
        Container mainLayout = getContentPane(); // Create the main content container for the JFrame

        // Create a JPanel for displaying playing cards in a 2x5 grid layout
        JPanel cardPanel = new JPanel(new GridLayout(2, 5));

        // Create and add JLabels with card images to the cardPanel
        for (int i = 0; i < 10; i++) {
            // Create a JLabel with the image of an Ace of Clubs (using the Card class)
            JLabel label01 = new JLabel(new Card(Suit.clubs, Rank.ace).getImage());
            cardPanel.add(label01); // Add the JLabel to the cardPanel
        }

        mainLayout.add(cardPanel, BorderLayout.CENTER); // Add the cardPanel to the main layout's center
        pack(); // Automatically adjust the frame size based on its contents
        setVisible(true); // Make the JFrame visible
    }

    // The main method to start the application
    public static void main(String[] $) {
        // Run the GUI construction in the event-dispatching thread for thread safety
        SwingUtilities.invokeLater(() -> new GameWindow());
    }
}
