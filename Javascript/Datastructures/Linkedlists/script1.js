class LinkedList{
    constructor(){
        // this.nodes = [];
        this.head = null; // first element of the list
        this.tail = null; // second element of the list
    }

    find(value){
        if(!this.head){
            return;
        }

        let currentNode = this.head;

        while(currentNode){
            if(currentNode.value === value){
                return currentNode;
            }
            currentNode = currentNode.next;
        }
        return null;
    }

    append(value) {
        const newNode = {value: value, next: null};

        if(this.tail){
            this.tail.next = newNode;
        }
        this.tail = newNode;
        if(!this.head){
            this.head = newNode;
        }
    }

    delete(value){
        if (!this.head) {
            return;
        }

        while(this.head && this.head.value === value ){
            this.head = this.head.next;
        }

        let currentNode = this.head;

        while (currentNode.next){
            if(currentNode.next.value === value){
                currentNode.next = currentNode.next.next;
            }else{
                currentNode = currentNode.next
            }
        }

        if(this.tail.value === value){
            this.tail = currentNode;
        }
    }

    prepend(value){
        const newNode = {value: value, next: this.head };

        this.head = newNode;
        if(!this.tail){
            this.tail = newNode;
        }
    }

    insertAfter(value, afterValue){
        const existingNode = this.find(afterValue);

        if(existingNode){
            const newNode = { value: value, next: existingNode.next};
            existingNode.next = newNode;
        }
    }
    toArray(){
        const elements = [];

        let currentNode = this.head;
        while(currentNode){
            elements.push(currentNode);
            currentNode = currentNode.next;
        }

        return elements;
    }
}

const list = new LinkedList();

list.append(1);
list.append("Hello");
list.append('max');
list.append(true);
list.append(18.52);
list.prepend(25)

console.log("Total elements ==> ",list.toArray());

list.prepend(1);
list.prepend(2);
list.prepend(3);
list.prepend(4);
list.prepend(5);

console.log("Total elements ==> ",list.toArray());

list.delete('max')
list.delete(25)
console.log("Total elements ==> ",list.toArray());

console.log("Finding elements ==> ",list.find(1));
console.log("Finding elements ==> ",list.find(10));

list.insertAfter("Dharan",3)
console.log("Total elements ==> ",list.toArray());
list.insertAfter("Kumar",2)
console.log("Total elements ==> ",list.toArray());