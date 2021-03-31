package ObjectClass;

class Book{
    private String title;
    private String author;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    /*
     * 객체에 대한 정보를 표현할 때 toString()을 overriding 함
     * */
    @Override
    public String toString() {
        return title + ", " + author;
    }
}

public class BookTest {
    public static void main(String[] args) {

        Book book = new Book("데미안", "헤르만헤세");
        System.out.println(book);
        String a = "hi";
        System.out.println(a.equals("hi"));

    }
}

