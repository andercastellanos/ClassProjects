public class TwoPair extends HandCategory {
    Rank higher;
    Rank lower;

    public TwoPair(Rank higher, Rank lower) {
        this.higher = higher;
        this.lower = lower;
    }

    @Override
    public String toString() {
        return "TwoPair [higher=" + higher + ", lower=" + lower + "]";
    }

    @Override
    int compareRank(Object right0) {
        TwoPair right = (TwoPair) right0;
        int high = higher.compareTo(right.higher);
        if (high == 0) {
            return lower.compareTo(right.lower);
        } else {
            return high;
        }
    }

    @Override
    int category() {
        return 8;
    }

}
