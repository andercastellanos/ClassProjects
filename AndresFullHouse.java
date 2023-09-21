public class FullHouse extends HandCategory { //The FullHouse class is being defined and it extends (or inherits from) another class called HandCategory.
    // This means that FullHouse is a subtype of HandCategory
    //and will inherit all of its properties and methods unless explicitly overridden.
    
    Rank highest; // This declares an instance variable named highest of type Rank. 
    //This variable will store the highest rank within the "Full House" hand.

    public FullHouse(Rank highest) { // Contructor for FullHouse taking parameter highest of type rank 
        this.highest = highest;
        // this.highest is an instance variable of the full house class 
        //This line is assigning the value of the highest parameter (the value passed into the constructor) 
        //to the highest instance variable of the current FullHouse object.
    }

    @Override // overriding the ToString() function 
    public String toString() {
        return "FullHouse [highest=" + highest + "]"; 
//The method returns a string that is the highest.
    }

    @Override
    int compareRank(Object right0) { //  This method is declared to return an int and takes an argument of type Object named right0.
        //The method is intended to compare the rank of the current object with the rank of another object.
        
        FullHouse right = (FullHouse) right0;
        
        // This part is attempting to cast the right0 object to the type FullHouse.
        
        return highest.compareTo(right.highest); // return the highest when compared to the right.highest 
    }

    @Override
    //This is a Java annotation which indicates that the method is intended to override a method in a superclass or interface.
    
    int category() { //defines a method named category that returns an integer (int).
     
        return 4;

        // this seems to be a way to categorize or rank the FullHouse hand type. 
        //The specific value 4 likely has some significance in terms of gameplay or hand ranking. 
        //For example, maybe different hand types return different values to denote their strength or type.
    }

}
