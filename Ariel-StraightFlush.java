// Ariel

public class StraightFlush extends HandCategory {
    Rank highest;
    Suit suit;

    public StraightFlush(Rank highest, Suit suit) {
        this.highest = highest;
        this.suit = suit;
    }

    @Override
    public String toString() {
        return "StraightFlush [highest=" + highest + ", suit=" + suit + "]";
    }

    @Override
    int compareRank(Object right0) {
        StraightFlush right = (StraightFlush) right0;
        int high = highest.compareTo(right.highest);
        if (high == 0) {
            return suit.compareTo(right.suit);
        } else {
            return high;
        }
    }

    @Override
    int category() {
        // TODO Auto-generated method stub
        return 2;
    }

}
