#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "lists.h"
/**
 * is_palindrome - hecks if a singly linked list is a palindrome
 * @head: list head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (0);
}
