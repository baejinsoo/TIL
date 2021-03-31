package StringClass;

public class StringTest {
    public static void main(String[] args) {
        /*
        * 힙 메모리는 생성될 때마다 다른 주소 값을 가지지만, 상수 풀의 문자열은 모두 같은 주소 값을 가짐
        * */
        String str1 = new String("abc"); // 힙 메모리에 인스턴스로 생성되는 경우
        String str2 = new String("abc");
        System.out.println(str1 == str2);

        String str3 = "abc"; // 상수 풀(constant pool)에 있는 주소를 참조하는 경우
        String str4 = "abc";
        System.out.println(str3 == str4);

        /*
        * 한번 생성된 String 은 불변(immutable)
        * String 을 연결하면 기존 String 에 연결되는 것이 아닌 새로운 문자열이 생성됨(메모리 낭비)
        * */
        String java = new String("java");
        String android = new String("android");
        System.out.println("\n"+System.identityHashCode(java));
        java = java.concat(android);

        System.out.println(java);
        System.out.println(System.identityHashCode(java));
    }

}
