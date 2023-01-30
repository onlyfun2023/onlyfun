/*
 * @Author: gerrardlt 305690790@qq.com
 * @Date: 2023-01-28 00:03:56
 * @LastEditors: gerrardlt 305690790@qq.com
 * @LastEditTime: 2023-01-29 01:21:06
 * @FilePath: \quhu\src\api\special\special.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
import request from '@/utils/request'

export function subscriptions (data) {
  return request({
    url: '/subscriptions',
    method: 'post',
    data
  })
}

export function post (data) {
  return request({
    url: '/post',
    method: 'post',
    data
  })
}
// 获取所有文章
export async function getArticles (data) {
  return request({
    baseURL: '/steem',
    // url: '/bridge.get_ranked_posts',
    method: 'post',
    data
  })
}
// 获取文章内容
export async function getArticleDetail (data) {
  return request({
    baseURL: '/steem',
    // url: '/bridge.get_discussion',
    method: 'post',
    data
  })
}
