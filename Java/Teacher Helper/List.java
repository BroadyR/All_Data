//class mate revised previous list class I made since it had bugs i could not personally fix
public class List<Type> {
    public static final int MAX_SIZE = 50;

    private Node<Type> head;
    private Node<Type> tail;
    private Node<Type> curr;
    private int num_items;

   // constructor
   public List() {
        head = new Node<>();
        tail = new Node<>();
        curr = new Node<>();
        num_items = -1;
    }

   public List(List<Type> l) {
        Node<Type> n = l.head;

        this.head = new Node<>();
        this.tail = new Node<>();
        this.curr = new Node<>();
        this.num_items = -1;

        while (n != null) {

            if (n.getData() != null) {
                this.InsertAfter(n.getData());
                n = n.getLink();

            } else {
                n = n.getLink();
            }
        }
    }

    // navigates to the beginning of the list
    public void First() {
        curr.setLink(head.getLink());
    }

    public void setCount(int a) {
        curr.getLink().setCount(a);
    }

    public int geCount() {
        return curr.getLink().getCount();
    }

    // navigates to the end of the list
    // the end of the list is at the last valid item in the list
    public void Last() {
        curr.setLink(tail.getLink());
    }

    // navigates to the specified element (0-index)
    // this should not be possible for an empty list
    // this should not be possible for invalid positions
    public void SetPos(int pos) {
        if (head.getLink() == null) {
            return;
        }
        if (pos > num_items) {
            return;
        }
        First();
        for (int i = 0; i < pos; i++) {
            Next();
        }
    }

    // navigates to the previous element
    // this should not be possible for an empty list
    // there should be no wrap-around
    public void Prev() {
        if (num_items == 0 || num_items == -1) {
            return;
        }
        Node n = new Node();
        n.setLink(head);
        for (int i = 0; i <= num_items; i++) {
            if (n.getLink().getLink() == curr.getLink()) {
                curr.setLink(n.getLink());
                return;
            }
            n.setLink(n.getLink().getLink());
        }
        curr.setLink(n.getLink());
    }


    // navigates to the next element
    // this should not be possible for an empty list
    // there should be no wrap-around
    public void Next() {
        if (num_items == 0 || num_items == -1) {
            return;
        }
        if (curr.getLink() == null) {
            return;
        }
        if(curr.getLink() == tail.getLink()){
            return;
        }
        curr.setLink(curr.getLink().getLink());
    }

    // returns the location of the current element (or -1)
    public int GetPos() {
        Node n = new Node();
        n = head;
        int index = 0;
        for (int i = 0; i <= num_items; i++) {
            if (n.getLink() == curr.getLink()) {
                return index;
            }
            index++;
            n = n.getLink();
        }
        return -1;
    }

    // returns the value of the current element (or null)
    public Type GetValue() {
        Type a = null;
        if (curr.getLink() == head) {
            Next();
        }
        if (curr.getLink() != null) {

            a = curr.getLink().getData();
        }

        return a;
    }

    // returns the size of the list
    // size does not imply capacity
    public int GetSize() {
        return num_items+1;
    }

    // inserts an item before the current element
    // the new element becomes the current
    // this should not be possible for a full list
    public void InsertBefore(Type data) {
        if (num_items+1 >= MAX_SIZE) {
            return;
        }
        Node n = new Node();
        n.setData(data);
        if (head.getLink() == null) {
            head.setLink(n);
            n.setLink(curr.getLink());
            curr.setLink(n);
            tail.setLink(n);
            num_items++;
        } else if (head.getLink() == tail.getLink()) {
            head.setLink(n);
            n.setLink(curr.getLink());
            curr.setLink(n);
            num_items++;
        } else if (head.getLink() == curr.getLink()) {

            n.setLink(head.getLink());
            head.setLink(n);
            curr.setLink(n);
            num_items++;
        } else {
            Prev();

            n.setLink(curr.getLink().getLink());
            curr.getLink().setLink(n);
            curr.setLink(n);
            num_items++;
        }
    }

    // inserts an item after the current element
    // the new element becomes the current
    // this should not be possible for a full list
    public void InsertAfter(Type data) {
        if (num_items+1 == MAX_SIZE) {
            return;
        }
        Node n = new Node();
        n.setData(data);
        if (head.getLink() == null) {
            head.setLink(n);
            curr.setLink(n);
            tail.setLink(n);
            num_items++;

        } else if (curr.getLink() == tail.getLink()) {
            curr.getLink().setLink(n);
             tail.setLink(n);// why does tail.setlink() change head
            curr.setLink(n);
            num_items++;
        } else {

            n.setLink(curr.getLink().getLink());
            curr.getLink().setLink(n);
            curr.setLink(n);
            num_items++;
        }
    }
    // removes the current element
    // this should not be possible for an empty list
    public void Remove()
    {
        if(head.getLink() == null){
            return;
        }
        if(curr.getLink() == null){
            return;
        }
        if (head.getLink() == tail.getLink()){
            curr.setLink(null);
            head.setLink(null);
            tail.setLink(null);
            num_items=-1;//dont want to set the list length to negative values as we empty the list

        }
        else if (curr.getLink() == tail.getLink()){
            Prev();
            tail.setLink(curr.getLink());
            curr.getLink().setLink(null);
            num_items -=1;// wow that was making replacing hard
        }
        else if(curr.getLink() == head.getLink()) {
            head.setLink(curr.getLink().getLink());
            curr.setLink(head.getLink());
            num_items -=1;        }

        else {
            Prev();
            curr.getLink().setLink(curr.getLink().getLink().getLink());
            Next();
            num_items -=1;
        }
    }

    // replaces the value of the current element with the specified value
    // this should not be possible for an empty list
    public void Replace(Type data)
    {
        if(head.getLink() == null){
            return;
        }
        if(curr.getLink() == null){
            return;
        }
        curr.getLink().setData(data);
    }

    // returns if the list is empty
    public boolean IsEmpty()
    {
        boolean response = false;
        if (head.getLink() == null){
            response = true;
        }
        return response;
    }

    // returns if the list is full
    public boolean IsFull()
    {
        boolean response = false;
        if (num_items+1 >= MAX_SIZE){
            response = true;
        }
        return response;
    }

    // returns if two lists are equal (by value)
    public boolean Equals(List<Type> l) {
        List a = new List(this);
        List b = new List(l);
        a.First();
        b.First();
        boolean response = true;
        if (a.GetSize() != b.GetSize()) {
            return response = false;
        }
        for (int i = 0; i < a.GetSize(); i++) {
            if (a.GetValue()!= b.GetValue()) {
                response = false;
            }
            a.Next();
            b.Next();
        }
        return response;
    }
    // returns the concatenation of two lists
    // l should not be modified
    // l should be concatenated to the end of *this
    // the returned list should not exceed MAX_SIZE elements
    // the last element of the new list is the current
    public List<Type> Add(List<Type> l)
    {
        List<Type> response = new List<>(this);
        Node<Type> n = l.head;
        response.Last();

        while (n != null && num_items < MAX_SIZE)
        {
            if(n.getData() != null){
                response.InsertAfter(n.getData());
                n = n.getLink();}
            else {
                n = n.getLink();}
        }
        return response;
    }

    public String toString()
    {
        String response = "";
        if (head.getLink() == null){
            return response = "NULL";
        }

        Node n = head.getLink();
        int i = 0;
        while (n.getLink() != null && n.getData() != null){
            response = response +" data = "+n.getData();
            n = n.getLink();
            i++;
        }
        if (n.getData() != null){
            response = response +" data = "+n.getData();
        }

        return response;
    }
}