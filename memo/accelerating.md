# Accelerating

## IO-Intensive

- Web Scraping: 请求占用主要时间，解析和储存时间较少。可以使用多线程／协程／异步请求- 单解析 - 单储存模式



## Compute-Intensive

- Computation：读入和读出占用时间较少，计算占用时间较多。可以使用单进程读入 - 多进程计算 - 单进程储存模式