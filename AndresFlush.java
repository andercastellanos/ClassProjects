public class Flush extends HandCategory {
    Rank highest;

    public Flush(Rank highest) {
        this.highest = highest;
    }

    @Override
    public String toString() {
        return "Flush [highest=" + highest + "]";
    }

    @Override
    int compareRank(Object right0) {
        Flush right = (Flush) right0;
        return highest.compareTo(right.highest);
    }

    @Override
    int category() {
        // TODO Auto-generated method stub
        return 5;
    }

}
