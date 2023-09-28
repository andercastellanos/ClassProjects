import java.awt.Image;
import java.util.HashMap;

import javax.swing.ImageIcon;

public class Card {
    final Suit suit; // Represents the suit of the Card, i.e. Hearts, Spades, Clubs and Diamonds
    final Rank rank; // Represents the rank of the Card, i.e. 2, 3, Ace, etc

    // Constructor to initialize a card object with a specific suit and rank
    public Card(Suit suit, Rank rank) {
        this.suit = suit; 
        this.rank = rank;
    }

    // Override the toString method to provide a custom string representation of a Card
    @Override
    public String toString() {
        return "Card [" + suit + " " + rank + "]";
    }

    // Override the hashCode method to generate a unique hash code for each Card object
    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((suit == null) ? 0 : suit.hashCode());
        result = prime * result + ((rank == null) ? 0 : rank.hashCode());
        return result;
    }

    // Override the equals method to compare two Card objects for equality
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

    // Static HashMap to store Card objects as keys and their associated ImageIcons as values
    static HashMap<Card, ImageIcon> images;
   // Static initialization block to populate the 'images' HashMap with Card images
    static {
        images = new HashMap<>();
        for (Rank rank : Rank.values()) {
            for (Suit suit : Suit.values()) {
                // Create a Card object for the current suit and rank
                Card card = new Card(suit, rank);
                // Generate the file name for the image based on suit and rank
                String name = "images/" + rank.fileSection() + "_of_" + suit.fileSection() + ".png";
                // Create an ImageIcon from the image file
                ImageIcon icon = new ImageIcon(name);
                // Scale down the ImageIcon to a smaller size
                icon = new ImageIcon(icon.getImage().getScaledInstance(500 / 4, 726 / 4, Image.SCALE_SMOOTH));
                // Put the Card-ImageIcon pair into the 'images' HashMap
                images.put(card, icon);
            }
        }
    }

    // Method to get the ImageIcon associated with a Card
    ImageIcon getImage() {
        return images.get(this);
    }
}
