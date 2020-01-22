public class Heap {
    public static void main(String[] args) {

        HeapList one  = new HeapList();
        one.Insert(10);
        one.Insert(20);
        one.Insert(3);
        one.Insert(100);
        one.Insert(1);
        one.Print();
        one.Peek();
        one.Delete();
        one.Peek();
    }
}

class HeapList{
    Node Head ;
    class Node
    {
        int data ;
        Node next ;
        Node(int val)
        {
            data = val ;
        }
    }
    public void Insert(int num)
    {
        if(Head ==  null)
        {
            Node element =  new Node(num);
            Head = element;
        }
        else{

            Node trav = Head ;
            Node temp = Head ;
            Boolean check = false;

            while (trav != null)
            {
                if(trav.data > num)
                {
                    System.out.println("Checj"+trav.data+" "+num);
                    Node n  = new Node(num);
                    if(trav == Head)
                    {
                        Head =  n ;
                        n.next = trav ;
                    }
                    else{
                        temp.next =   n ;
                        n.next = trav ;
                    }

                    check = true;
                    break;
                }
                else{
                    temp = trav ;
                    trav = trav.next ;
                }

            }
            if(check == false)
            {
                Node n  = new Node(num);
                temp.next = n ;
            }
        }

    }
    public void Print()
    {
        Node trav  = Head ;
        while (trav != null)
        {
            System.out.println(trav.data);
            trav = trav.next ;
        }
    }
    public void Peek()
    {
        System.out.println("The Smallest Number is: "+Head.data);
    }
    public void Delete(){
        Node temp = Head ;
        System.out.println("Delted: "+ temp.data);
        Head  =  temp.next ;
    }

}