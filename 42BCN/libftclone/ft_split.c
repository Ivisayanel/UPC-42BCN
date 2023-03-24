/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@42barcelona.com>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/28 12:13:48 by isanchez          #+#    #+#             */
/*   Updated: 2023/01/28 12:31:08 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static	char	**do_split(char const *s, char c, char **split, int len)
{
	static int	j = 0;
	static int	i = 0;
	static int	n = 0;

	if (n == len)
		return (split);
	else if (s[n] == c)
	{
		if (n != 0 && s[n - 1] != c && s[n + 1] != 0)
		{
			i++;
			j = 0;
		}
		n++;
		return (do_split(s, c, split, len));
	}
	else
	{
		split[i][j] = s[n];
		j++;
		n++;
		return (do_split(s, c, split, len));
	}
}

static void	free_all(char **split, size_t *str_len)
{
	int	i;

	i = 0;
	if (split != NULL)
	{
		while (split[i] != NULL)
		{
			free(split[i]);
			i++;
		}
		free(split[i]);
	}
	free(split);
	free(str_len);
}

static char	**create_split(char **split, size_t *str_len)
{
	size_t	i;

	i = 0;
	split = malloc((str_len[0] + 1) * sizeof(char *));
	if (split == NULL || str_len == NULL)
	{
		free_all(split, str_len);
		return (NULL);
	}
	split[str_len[0]] = NULL;
	while (i < str_len[0] && str_len != NULL && split != NULL)
	{
		split[i] = malloc((str_len[i + 1] + 1) * sizeof(char));
		if (split[i] == NULL)
		{
			free_all(split, str_len);
			break ;
		}
		split[i][str_len[i + 1]] = 0;
		i++;
	}
	free(str_len);
	return (split);
}

char	**ft_split(char const *s, char c)
{
	static char	**split;
	static int	iter;
	int			len;
	size_t		*str_len;

	len = ft_strlen(s);
	str_len = ft_calloc(((len / 2 + len % 2) + 1), sizeof(int));
	if (str_len == NULL)
		free_all(NULL, str_len);
	while (iter < len && str_len != NULL)
	{
		if (s[iter] != c)
		{
			str_len[0]++;
			while ((s[iter] != c) && s[iter])
			{
				str_len[str_len[0]]++;
				iter++;
			}
		}
		iter++;
	}
	split = create_split(split, str_len);
	do_split(s, c, split, len);
	return (split);
}
