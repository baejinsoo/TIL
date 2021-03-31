package ObjectClass;

public class EqualsTest {
    public static void main(String[] args) throws CloneNotSupportedException {
        student std1 = new student(100, "Lee");
        student std2 = new student(100, "Lee");
        student std3 = std2;

        System.out.println(std1.hashCode()); // hashCode()를 sudentNum이 되도록 overriding 해보기
        System.out.println(std2.hashCode());
        System.out.println(std3.hashCode());
        System.out.println(System.identityHashCode(std1)); // 실제 가상메모리 값 출력
        System.out.println(System.identityHashCode(std2));
        System.out.println(System.identityHashCode(std3));
        System.out.println();
        System.out.println(std1 == std2); // false
        System.out.println(std1.equals(std2)); // false -> equals : 두개의 주소값이 같으냐
        System.out.println(std2 == std3); // true
        System.out.println();

        student copyStudent = (student)std1.clone();
        System.out.println(copyStudent.toString()); // Exception in thread "main" java.lang.CloneNotSupportedException: ObjectClass.student
    }
}
