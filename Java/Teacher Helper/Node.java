public class Node<Type>
{
    private Type data;
    private Node<Type> link;
    private int count;

    // constructor
    public Node()
    {
        this.data = null;
        this.count = 1;
        this.link = null;
    }

    // accessor and mutator for the data component
    public Type getData()
    {
        return this.data;
    }

    public void setData(Type data)
    {
        this.data = data;
    }
    //accersor and mutator for the count
    public int getCount(){
        return this.count;
    }
    public void setCount(int data){
        this.count = data;
    }
    // accessor and mutator for the link component
    public Node<Type> getLink()
    {
        return this.link;
    }

    public void setLink(Node<Type> link)
    {
        this.link = link;
    }
}