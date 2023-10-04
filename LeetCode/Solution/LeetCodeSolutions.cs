using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Diagnostics.Metrics;
using System.Linq;
using System.Linq.Expressions;
using System.Runtime.ExceptionServices;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Solution
{
	public class LeetCodeSolutions
	{
		public string ReorganizeString(string s)
		{
			Dictionary<char, int> charactersShowing = new Dictionary<char, int>();

			foreach (char symbol in s) // O(n)
			{
				if (charactersShowing.ContainsKey(symbol))
				{
					charactersShowing[symbol]++;
				}
				else
				{
					charactersShowing.Add(symbol, 1);
				}
			}

			if (charactersShowing.Values.Max() > (s.Length + 1)/2) 
			{
				return "";
			}

			charactersShowing = charactersShowing
				.OrderByDescending(x => x.Value)
				.ThenBy(x => x.Key)
				.ToDictionary(x => x.Key, x => x.Value);
		
			string result = string.Empty;

			while (charactersShowing.Values.Sum() > 0)
			{
				var mostCommonChar = charactersShowing
					.Where(x => x.Value > 0)
					//.OrderByDescending(x => x.Value)
					//.ThenBy(x => x.Key)
					.Select(x => x.Key)
					.FirstOrDefault();
				var secondMostCommonChar = charactersShowing
					.Where(x => x.Value > 0)
					//.OrderByDescending(x => x.Value)
					//.ThenBy(x => x.Key)
					.Select(x => x.Key)
					.Skip(1)
					.FirstOrDefault();

				result += mostCommonChar.ToString();
				

				charactersShowing[mostCommonChar]--;
				if (secondMostCommonChar != 0) 
				{
					result += secondMostCommonChar.ToString();
					charactersShowing[secondMostCommonChar]--;
				}

			}

			return result;
		}
	}
}
