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

    public GameWindow() throws HeadlessException {
        super("Poker");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        Container mainLayout = getContentPane();

        JPanel cardPanel = new JPanel(new GridLayout(2, 5));

        for (int i = 0; i < 10; i++) {
            JLabel label01 = new JLabel(new Card(Suit.clubs, Rank.ace).getImage());
            cardPanel.add(label01);
        }

        mainLayout.add(cardPanel, BorderLayout.CENTER);
        pack();
        setVisible(true);
    }

    public static void main(String[] $) {
        SwingUtilities.invokeLater(() -> new GameWindow());
    }
}
