#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject list
 */
void print_python_list(PyObject *p)
{ 
	Py_ssize_t i, size;
	PyObject *obj;

    if (!PyList_Check(p))
    {
        printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    printf("[*] Python list info\n  Size of the Python List = %ld\n  Allocated = %ld\n", size, ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        obj = ((PyListObject *)p)->ob_item[i];
        printf("  Element %ld: %s\n", i, ((PyObject *)(obj))->ob_type->tp_name);
    }
}
/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: pointer to PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    char *str;

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n  Size: %ld\n  Trying string: %s\n", ((PyVarObject *)p)->ob_size, ((PyBytesObject *)p)->ob_sval);

    size = ((PyVarObject *)p)->ob_size > 10 ? 10 : ((PyVarObject *)p)->ob_size + 1;
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  First %ld bytes: ", size - 1);
    for (i = 0; i < size - 1; i++)
        printf("%02hhx ", str[i]);
    printf("%02hhx\n", str[i]);
}

/**
 * print_python_float - prints some basic info about Python float objects
 * @p: pointer to PyObject float
 */
void print_python_float(PyObject *p)
{
    char *str;

    if (!PyFloat_Check(p))
    {
        printf("[ERROR] Invalid Float Object\n");
        return;
    }

    str = PyOS_double_to_string(PyFloat_AsDouble(p), 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("[.] float object info\n  Value: %s\n", str);
}

