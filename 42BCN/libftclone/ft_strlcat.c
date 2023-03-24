/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: isanchez <isanchez@42barcelona.com>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/24 09:23:24 by isanchez          #+#    #+#             */
/*   Updated: 2023/03/16 17:39:40 by isanchez         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t dstsize)
{
	size_t	i;
	size_t	p;
	size_t	dst_size;
	size_t	src_size;

	src_size = ft_strlen(src);
	dst_size = ft_strlen(dst);
	if ((dstsize > 0) && (dst_size < dstsize))
	{
		i = dst_size;
		p = 0;
		while (src[p] && i < (dstsize - 1))
		{
			dst[i] = src[p];
			p++;
			i++;
		}
		dst[i] = 0;
	}
	if (dst_size > dstsize)
		dst_size = dstsize;
	return (src_size + dst_size);
}
