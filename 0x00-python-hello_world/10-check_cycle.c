#include "lists.h"
/**
 * check_cycle - check_cycle
 * @list: list
 * @node: node to be checked
 * @i: index
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{

	int idx = 0, occurrence = 0;
	listint_t *node, *head = list;


	while (head != NULL)
	{
		node = head->next;
		while (node !=NULL)
		{
			if (head == node)
				return (1);
			node = node->next;
		}
		head = head->next;
	}

	return (0);
}
