using System;
using System.Collections.Generic;
using System.Linq;

namespace tree
{
    class Program
    {
	public static void Height(int[] parent, int i, int[] depth) 
	{ 
		if (depth[i] != 0) 
		{ 
			return; 
		} 

		if (parent[i] == -1) 
		{ 
			depth[i] = 1; 
			return; 
		} 

		 
		if (depth[parent[i]] == 0) 
		{ 
			Height(parent, parent[i], depth); 
		} 

		depth[i] = depth[parent[i]] + 1; 
	} 

	public static int findHeight(int[] parent, int n) 
	{ 
		int[] depth = new int[n]; 
		
		for (int i = 0; i < n; i++) 
		{ 
			depth[i] = 0; 
		} 


		for (int i = 0; i < n; i++) 
		{ 
			Height(parent, i, depth); 
		} 

		int height2 = depth[0]; 
		for (int i = 1; i < n; i++) 
		{ 
			if (height2 < depth[i]) 
			{ 
				height2 = depth[i]; 
			} 
		} 
		return height2; 
	} 

        static void Main(string[] args)
        {

        string val = Console.ReadLine();
        int n= Convert.ToInt32(val);
        
		string myString = Console.ReadLine(); 
        int[] nums = Array.ConvertAll(myString.Split(' '), int.Parse);

        Console.WriteLine(findHeight(nums, n));
        }
    }
}


