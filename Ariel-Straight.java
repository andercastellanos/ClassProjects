public class Straight extends HandCategory {
    Rank highest;

    public Straight(Rank highest) {
        this.highest = highest;
    }

    @Override
    public String toString() {
        return "Straight [highest=" + highest + "]";
    }

    @Override
    int compareRank(Object right0) {
        Straight right = (Straight) right0;
        return highest.compareTo(right.highest);
    }

    @Override
    int category() {
        return 6;
    }

}
