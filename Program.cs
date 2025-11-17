using System;
using System.Collections.Generic;

namespace TodoListApp
{
    class Program
    {
        static List<string> todos = new List<string>();

        static void Main(string[] args)
        {
            Console.WriteLine("TODO LIST APP (with errors, ELK error logging demo)");
            while (true)
            {
                try
                {
                    Console.WriteLine("\n1. Add Todo\n2. List Todos\n3. Remove Todo\n4. Exit");
                    Console.Write("Choose option: ");
                    int option = int.Parse(Console.ReadLine()); // Error: no validation

                    if (option == 1)
                    {
                        Console.Write("Enter todo item: ");
                        string todo = Console.ReadLine();
                        todos.Add(todo);
                    }
                    else if (option == 2)
                    {
                        Console.WriteLine("Your todos:");
                        for (int i = 0; i <= todos.Count; i++) // Error: off-by-one (should be i < todos.Count)
                        {
                            Console.WriteLine($"{i+1}. {todos[i]}");
                        }
                    }
                    else if (option == 3)
                    {
                        Console.Write("Enter todo number to remove: ");
                        int removeIndex = int.Parse(Console.ReadLine());
                        todos.RemoveAt(removeIndex); // Error: no -1 adjustment, index validation missing
                    }
                    else if (option == 4)
                    {
                        break;
                    }
                    else
                    {
                        throw new Exception("Invalid option chosen."); // Not necessary but for demo purposes
                    }
                }
                catch (Exception ex)
                {
                    // Simulate sending to ELK
                    Console.WriteLine($"[ELK] Error: {ex.Message}");
                }
            }
        }
    }
}
