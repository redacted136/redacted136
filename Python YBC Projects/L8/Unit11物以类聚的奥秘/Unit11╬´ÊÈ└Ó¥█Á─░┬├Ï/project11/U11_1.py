from sklearn.cluster import KMeans
from kmeans import main

class Solution():
    def kmeans_clustering(self, train_data):
        # 实例化K-means模型，设置聚类数量和随机状态
        model = KMeans(n_clusters=5,random_state=0)
        # 将数据输入模型进行训练
        model.fit(train_data)
        # 根据相似性进行聚类
        result = model.predict(train_data)
        return result

solution = Solution()
main(solution)


