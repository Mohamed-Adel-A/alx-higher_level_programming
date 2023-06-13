#include <object.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - print_python_list_info
 * @p: PyObject 
 * Return: void
 */
 
 void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyListObject *pyobj = (PyListObject *)p;
	long int list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", pyobj->allocated);
	for (i = 0; i < list_size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(pyobj->ob_item[i])->tp_name);
}
