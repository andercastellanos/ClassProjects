public abstract class HandCategory implements Comparable<HandCategory> {
    abstract int compareRank(Object right);

    abstract int category();

    public int compareTo(HandCategory right) {
        if (category() < right.category()) {
            return 1;
        } else if (category() > right.category()) {
            return -1;
        } else {
            return this.compareRank(right);
        }
    }
}
