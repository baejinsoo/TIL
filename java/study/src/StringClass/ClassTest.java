package StringClass;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

public class ClassTest {
    public static void main(String[] args) throws ClassNotFoundException, IllegalAccessException, InstantiationException, NoSuchMethodException, InvocationTargetException {
        Class c1 = Class.forName("StringClass.Person");
        Person person = (Person) c1.newInstance();

        person.setName("Lee");
        System.out.println(person);
        /*
        * Local에 Person이 없을 때 (아래방법과 Person kim = new Person("Kim); 은 같음)
        * */
        Class c2 = person.getClass(); // getClass() 사용하려면 이미 인스턴스가 있는경우
        Person p = (Person) c2.newInstance();
        System.out.println(p);

        Class[] parameterTypes = {String.class};
        Constructor cons = c2.getConstructor(parameterTypes);

        Object[] initargs = {"Kim"};
        Person kimPerson = (Person) cons.newInstance(initargs);
        System.out.println(kimPerson);
    }
}
