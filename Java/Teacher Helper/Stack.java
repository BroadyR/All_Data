public class Stack extends List {
    public <Type> void Push(Type a){
        super.First();
        super.InsertBefore(a);
    }
    public String Pop(){
        String response = (String) super.GetValue();
        super.First();
        super.Remove();

        return response;
    }
    public String Peek(){
        super.First();
        if(super.GetValue() == null){
            return null;
        }
        String t = (String) super.GetValue();
        return t;
    }
}