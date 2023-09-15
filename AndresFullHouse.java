public class FullHouse extends HandCategory {
    Rank highest;

    public FullHouse(Rank highest) {
        this.highest = highest;
    }

    @Override
    public String toString() {
        return "FullHouse [highest=" + highest + "]";
    }

    @Override
    int compareRank(Object right0) {
        FullHouse right = (FullHouse) right0;
        return highest.compareTo(right.highest);
    }

    @Override
    int category() {
        // TODO Auto-generated method stub
        return 4;
    }

}
