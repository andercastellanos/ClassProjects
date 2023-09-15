import java.awt.Image;
import java.util.HashMap;

import javax.swing.ImageIcon;

public class Card {
    final Suit suit;
    final Rank rank;

    public Card(Suit suit, Rank rank) {
        this.suit = suit;
        this.rank = rank;
    }

    @Override
    public String toString() {
        return "Card [" + suit + " " + rank + "]";
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((suit == null) ? 0 : suit.hashCode());
        result = prime * result + ((rank == null) ? 0 : rank.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Card other = (Card) obj;
        if (suit != other.suit)
            return false;
        if (rank != other.rank)
            return false;
        return true;
    }

    static HashMap<Card, ImageIcon> images;
    static {
        images = new HashMap<>();
        for (Rank rank : Rank.values()) {
            for (Suit suit : Suit.values()) {
                Card card = new Card(suit, rank);
                String name = "images/" + rank.fileSection() + "_of_" + suit.fileSection() + ".png";
                ImageIcon icon = new ImageIcon(name);
                icon = new ImageIcon(icon.getImage().getScaledInstance(500 / 4, 726 / 4, Image.SCALE_SMOOTH));
                images.put(card, icon);
            }
        }
    }

    ImageIcon getImage() {
        return images.get(this);
    }
}
