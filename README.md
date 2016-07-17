![](http://www.brandsoftheworld.com/sites/default/files/styles/logo-thumbnail/public/092015/pokemongo.png?itok=LERVo0L9)  
# pymgo - 快成为神奇宝贝大师！
因为是私密项目, 所以想到什么加什么.主要信息来源都是reddit的讨论版：https://www.reddit.com/r/pokemongodev/.  

## 服务器通信
1. 数据加密  
  * 验证以外的用户和服务器的数据交互, 都是基于google的protocol buffer进行的序列化.服务器返回值的反序列化需要有相关工具, 和对应的类及引用类的proto文件, 主返回类是[ResponseEvelope](https://github.com/AeonLucid/POGOProtos/blob/0a36f8c9ef3194f028e1ab54a29011a51eeeaff8/pogo/Envelopes.proto).用户的请求也需要用序列化, 主请求类是[RequestEnvelop](https://github.com/AeonLucid/POGOProtos/tree/master/pogo/Requests).
  * 在没有对应proto文件情况下, 只能看到一堆的键值而无法理解具体内容, 但是哪怕是只有一部分的proto文件, 也足够读取到对应的键值的真实信息!
  * 外国人已经反反向工程处一些必须的.proto（比如根据地理位置的精灵分布）并且生成了对应的工具类.
  * 目前分析出来的proto还很少, 最新进展在[这里](https://github.com/AeonLucid/POGOProtos).
2. 通信过程
  * 一开始用户端会与服务器进行登录验证并拿到access token（此部分仅是JWT）.
  * 成功后进行第一次正式通信（此时开始都是protobuf）, 地址为 pgorelease.nianticlabs.com/plfe/rpc, 返回包括[Player](https://gist.github.com/anonymous/2fe78436f84d0ece1e182d388d12b1ea)/[Inventory](https://gist.github.com/anonymous/d4035099c4b46fa45740714436248ead)/[Settings](https://gist.github.com/anonymous/1f05df105102f7d70e6b6be40dcf68f7).具体内容可以点进去看, 都是用户数据.
  * 此次请求的返回本体中会包含一个值叫api_url, 类似pgorelease.nianticlabs.com/plfe/xxxxxxxx/rpc, 用以后续请求.
  * 之后客户端定期会发送类似heartbeat的请求, 包含有地理位置给服务器.服务器返回[Map](https://gist.github.com/anonymous/568fd0467ec73dc78a6e24fc8671bc06), 其中包含了地图相关的信息.
    * 其中有附近的小精灵, 野生小精灵, 据点以及刷新点信息.然后这些信息就可以用来渲染地图显示附近精灵.
    * 正常情况下返回的[NearbyPokemon](https://github.com/AeonLucid/POGOProtos/blob/master/pogo/Map/Pokemon/NearbyPokemon.proto)并不含有物理坐标, 只是离玩家的距离.玩家非常接近时会返回特殊对象[MapPokemon](https://github.com/AeonLucid/POGOProtos/blob/master/pogo/Map/Pokemon/MapPokemon.proto)/[WildPokemon](https://github.com/AeonLucid/POGOProtos/blob/master/pogo/Map/Pokemon/WildPokemon.proto), 含有坐标, 持续时间以及刷新id.

## 开发
1. 群众需求  
  * 最大的需求应该是显示附近的小精灵刷新, 下图是可视化地图的效果（仅本地使用）.
  ![](https://raw.githubusercontent.com/AHAAAAAAA/PokemonGo-Map/master/static/Screenshot%202016-07-16%2021.32.10.png)
2. 社区进度
  * 大量外国开发者每天都在快速迭代新的工具, 所以我们的项目也是尽量敏捷开发
  * 目前社区进度已经到了可视化地图的实现, 但是需要主动下载repo跑flask服务器.
  * 因此我们的实现也可以着重用一体化框架, 直接为用户抓取小精灵信息然后渲染地图.
3. 顾虑
  * 目前唯一能读取附近小精灵刷新的办法, 就是模拟和服务的对话, 这个是需要使用用户信息的.
  * 外国人的实现里, 用户信息是使用者自己输入然后本地服务器处理.在我们的实现里, 如果只是读取用户明暗信息的话, 是否会有各种隐私问题？
  * 就算不存储用户的账号信息, 这些敏感数据依然会是个巨大的隐患.要如何解决呢？


## 扩展阅读
* [Reddit的PMGO开发者区](https://www.reddit.com/r/pokemongodev/)
  * [服务器通信1](https://www.reddit.com/r/pokemongodev/comments/4svl1o/guide_to_pokemon_go_server_responses/)
  * [服务器通信2](https://www.reddit.com/r/pokemongodev/comments/4t7eqr/better_understanding_the_pokemongo_clientserver/)
  * [模拟服务器对话的讨论串](https://www.reddit.com/r/pokemongodev/comments/4t3lgh/githubwip_get_precise_location_of_all_nearby/?sort=new)
  * [可视化地图](https://www.reddit.com/r/pokemongodev/comments/4t80df/wip_pokemon_go_map_visualization_google_maps_view/)
* GitHub
  * [模拟服务器对话的python实现](https://github.com/leegao/pokemongo-api-demo)
  * [可视化地图的flask实现](https://github.com/AHAAAAAAA/PokemonGo-Map)
  * [protobuf的反向工程](https://github.com/AeonLucid/POGOProtos)
