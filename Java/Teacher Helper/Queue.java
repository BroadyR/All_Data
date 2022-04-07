public class Queue <Type> extends List {
    public void enqueue(Type a){
        super.Last();
        super.InsertAfter(a);
    }
    public String DeQueue(){
        super.First();
        String response = (String) super.GetValue();
        super.Remove();
        return (String) response;
    }

}