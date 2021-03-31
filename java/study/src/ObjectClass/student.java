package ObjectClass;

public class student implements Cloneable{

    private int studentNum;
    private String studentName;

    public student(int studentNum, String studentName) {
        this.studentNum = studentNum;
        this.studentName = studentName;
    }

    @Override
    public String toString() {
        return studentNum + ", " +studentName;
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    @Override
    public int hashCode() {
        return studentNum;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof student) {
            student std = (student)obj;
            if (this.studentNum == std.studentNum) {
                return true;
            } else return false;
        }
        return false;
    }
}
