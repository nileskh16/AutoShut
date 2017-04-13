#include<iostream>
#include<string.h>
using namespace std;

int editDist(string s1, string s2, int m, int n)
{
	int dp[m+1][n+1];
	
	for(int i=0; i<=m; i++)
		for(int j=0; j<=n; j++)
		{
			if(i==0)
				dp[i][j] = j;
			else if(j == 0)
				dp[i][j] = i;
			else if(s1[i-1] == s2[j-1])
				dp[i][j] = dp[i-1][j-1];
			else
				dp[i][j] = 1 + min(dp[i][j-1], min(dp[i-1][j-1], dp[i-1][j]));	
		}
	return dp[m][n];
}

int main()
{
	int t;
	string s1, s2;
	cin>>t;
	for(int i=0; i<t; i++)
	{
		s1 = ""; s2 = "";
		cin>>s1>>s2;
		cout<<editDist(s1, s2, s1.length(), s2.length())<<endl;
	}
	return 0;
}
