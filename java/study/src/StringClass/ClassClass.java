package StringClass;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class ClassClass {
    public static void main(String[] args) throws ClassNotFoundException {
        Class<?> c = Class.forName("java.lang.String");

        Constructor[] constructor = c.getConstructors();
        for (Constructor co : constructor) {
            System.out.println(co);
        }
        Method[] method = c.getMethods();
        for (Method mth : method) {
            System.out.println(mth);
        }

    }
}
