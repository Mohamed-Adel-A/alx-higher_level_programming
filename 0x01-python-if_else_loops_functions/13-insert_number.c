#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: list head
 * @number: number to be added
 *
 * Return: head or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = head, new_node, prv_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
			new_node.n = number;
	if (new_node == NULL)
		return (NULL);

	while(node != NULL)
	{
		if (number <= node->n)
		{
			if (node == head)
			{
				new_node.next = head;
				head = new_node;
			}
			else
			{
				new_node.next = node;
				prv_node->next = new_node;
			}
			break;
		}
		prv_node = node;
		node = node->next;			
	}
	return (head);
}
