class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


def create_poly():
    n = int(input("Enter number of terms: "))
    head = None
    tail = None

    for i in range(n):
        coeff = int(input("Enter coefficient: "))
        power = int(input("Enter power: "))
        new = Node(coeff, power)

        if head is None:
            head = new
            tail = new
        else:
            tail.next = new
            tail = new

    return head


def add_poly(p, q):
    head = None
    tail = None

    while p and q:
        if p.power == q.power:
            coeff = p.coeff + q.coeff
            if coeff != 0:
                new = Node(coeff, p.power)
                if head is None:
                    head = tail = new
                else:
                    tail.next = new
                    tail = new
            p = p.next
            q = q.next

        elif p.power < q.power:
            new = Node(p.coeff, p.power)
            if head is None:
                head = tail = new
            else:
                tail.next = new
                tail = new
            p = p.next

        else:
            new = Node(q.coeff, q.power)
            if head is None:
                head = tail = new
            else:
                tail.next = new
                tail = new
            q = q.next

    while p:
        new = Node(p.coeff, p.power)
        if head is None:
            head = tail = new
        else:
            tail.next = new
            tail = new
        p = p.next

    while q:
        new = Node(q.coeff, q.power)
        if head is None:
            head = tail = new
        else:
            tail.next = new
            tail = new
        q = q.next

    return head


def display(poly):
    while poly:
        print(f"{poly.coeff}x^{poly.power}", end="")
        if poly.next:
            print(" + ", end="")
        poly = poly.next
    print()


print("First Polynomial")
p = create_poly()

print("Second Polynomial")
q = create_poly()

print("First Polynomial:")
display(p)

print("Second Polynomial:")
display(q)

result = add_poly(p, q)

print("Resultant Polynomial:")
display(result)
