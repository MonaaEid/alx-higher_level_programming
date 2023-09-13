#include <stdio.h>
#include <Python.h>
/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->ob_base.ob_size);
	for (i = 0, size = PyList_Size(p); i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
    	}
}
/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{

	Py_ssize_t i, size;
	char *buffer;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
    	{
        	printf("  [ERROR] Invalid Bytes Object\n");
        	return;
    	}

	size = ((PyVarObject *)p)->ob_size;
    	buffer = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
    	printf("  trying string: %s\n", buffer);

	if (size > 10)
		size = 10;
	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
		printf(" %02x", buffer[i] & 0xff);
	printf("\n");
}
