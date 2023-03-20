import matplotlib.pyplot as plt
import numpy as np


class Topic():
    def __init__(self, desc):
        self.id = desc
        self.turn_desc = []
        self.p10_lmd = []
        self.p10_bert = []
        self.ndcg5_lmd = []
        self.ndcg5_bert = []
        self.ap_lmd = []
        self.ap_bert = []
        self.recall_var_lmd = []
        self.recall_var_bert = []
        self.precision_var_lmd = []
        self.precision_var_bert = []

topics = []

def reset():
    topics= []
    
def find_topic_name(topic_name):
    for i in range(0, len(topics)):
        if topics[i].id == topic_name:
            return topics[i]
    return None

def add_topic(topic_name):
    topic = find_topic_name(topic_name)
    topics.append(Topic(topic_name))
  


def add_turn(topic_name, t_desc):
    topic = find_topic_name(topic_name)
    topic.turn_desc.append(t_desc)

def add_p10(p10_parc, topic_name, algorithm):
    topic = find_topic_name(topic_name)
    if topic is None:
        topic = Topic(topic_name)
        topics.append(topic)
    if algorithm == 'Elastic Search':
        topic.p10_lmd.append(p10_parc)
    else:
        topic.p10_bert.append(p10_parc)


def add_ap(ap_parc, topic_name, algorithm):
    topic = find_topic_name(topic_name)
    if topic is None:
        topic = Topic(topic_name)
        topics.append(topic)
    if algorithm == 'Elastic Search':
        topic.ap_lmd.append(ap_parc)
    else:
        topic.ap_bert.append(ap_parc)


def add_ndcg5(ndcg5_parc, topic_name, algorithm):
    topic = find_topic_name(topic_name)
    if topic is None:
        topic = Topic(topic_name)
        topics.append(topic)
    if algorithm == 'Elastic Search':
        topic.ndcg5_lmd.append(ndcg5_parc)
    else:
        topic.ndcg5_bert.append(ndcg5_parc)


def add_recall_var(recall_var, topic_name, algorithm):
    topic = find_topic_name(topic_name)

    if topic is None:
        topic = Topic(topic_name)
        topics.append(topic)
    if algorithm == 'Elastic Search':
        topic.recall_var_lmd.append(recall_var)
    else:
        topic.recall_var_bert.append(recall_var)


def add_precision_var(precision_var, topic_name, algorithm):
    topic = find_topic_name(topic_name)

    if topic is None:
        topic = Topic(topic_name)
        topics.append(topic)
    if algorithm == 'Elastic Search':
        topic.precision_var_lmd.append(precision_var)
    else:
        topic.precision_var_bert.append(precision_var)

#plot p10

def plot_p10_per_topic(topic_name, n_turns):
    topic = find_topic_name(topic_name)
    print(len(topic.p10_lmd))
    print(len(topic.p10_bert))
    turns = min(len(topic.p10_lmd), n_turns)
    turns = min(len(topic.p10_bert), turns)
    plt.figure(frameon=False)
    
    plt.plot(topic.p10_lmd[:turns], topic.turn_desc[:turns], 'x', color="blue", label='Elastic Search')
    plt.plot(topic.p10_bert[:turns], topic.turn_desc[:turns], 'x', color="red", label='Bert')
    
    plt.legend(loc="upper right")
    plt.xlabel("P@10 topic " + str(topic_name))
    plt.grid()
    plt.savefig("P@10 topic " + str(topic_name))
    plt.show()
    plt.close()


def plot_p10(n_turns):
    p10_lmd = 0
    p10_bert = 0
    turns = np.zeros(n_turns)
    for topic in topics:
        topic_p10s = np.zeros(n_turns)
        topic_p10s[:len(topic.p10_lmd)] = topic.p10_lmd[:n_turns]
        p10_lmd += topic_p10s
        topic_p10s[:len(topic.p10_bert)] = topic.p10_bert[:n_turns]
        p10_bert += topic_p10s
        turns[:len(topic.p10_lmd)] += 1

    p10_lmd = (p10_lmd / len(turns))
    p10_bert = (p10_bert / len(turns))
    plt.figure(frameon=False)
    plt.plot(range(1, n_turns+1), p10_lmd, color="blue", label = 'Elastic Search')
    plt.plot(range(1, n_turns+1), p10_bert, color="red", label = 'Bert')
    plt.legend(loc="upper right")
    plt.xlabel("P@10")
    plt.grid()
    plt.savefig("P@10")
    plt.show()
    plt.close()


# plot ap

def plot_ap_per_topic(topic_name, n_turns):
    topic = find_topic_name(topic_name)
    turns = min(len(topic.ap_lmd), n_turns)
    plt.figure(frameon=False)
    plt.plot(topic.ap_lmd[:turns], topic.turn_desc[:turns], 'x', color="blue", label='Elastic Search')
    plt.plot(topic.ap_bert[:turns], topic.turn_desc[:turns], 'x', color="red", label='Bert')
    plt.legend(loc="upper right")
    plt.xlabel("AP topic " + str(topic_name))
    plt.grid()
    plt.savefig("AP topic " + str(topic_name))
    plt.show()
    plt.close()

def plot_ap(n_turns):
    ap_lmd = 0
    ap_bert = 0
    turns = np.zeros(n_turns)
    for topic in topics:
        topic_aps = np.zeros(n_turns)
        topic_aps[:len(topic.ap_lmd)] = topic.ap_lmd[:n_turns]
        ap_lmd += topic_aps
        topic_aps[:len(topic.ap_bert)] = topic.ap_bert[:n_turns]
        ap_bert += topic_aps
        turns[:len(topic.ap_lmd)] += 1

    ap_lmd = (ap_lmd / len(turns))
    ap_bert = (ap_bert / len(turns))
    plt.figure(frameon=False)
    plt.plot(range(1, n_turns+1), ap_lmd, color="blue", label = 'Elastic Search')
    plt.plot(range(1, n_turns+1), ap_bert, color="red", label = 'Bert')
    plt.legend(loc="upper right")
    plt.xlabel("AP")
    plt.grid()
    plt.savefig("AP")
    plt.show()
    plt.close()


# plot ndcg5

def plot_ndcg5_per_topic(topic_name, n_turns):
    topic = find_topic_name(topic_name)
    turns = min(len(topic.ndcg5_lmd), n_turns)
    plt.figure(frameon=False)
    plt.plot(topic.ndcg5_lmd[:turns],topic.turn_desc[:turns],'x',  color="blue", label='Elastic Search')
    plt.plot(topic.ndcg5_bert[:turns],topic.turn_desc[:turns],'x',  color="red", label='Bert')
    #plt.xticks(np.arange(0, 1.2, 0.2))
    plt.legend(loc="upper right")
    plt.xlabel("NDGC@5 topic " + str(topic_name))
    plt.grid()
    plt.savefig("NDGC@5 topic " + str(topic_name))
    plt.show()
    plt.close()

def plot_ndcg5(n_turns):
    ndcg5_lmd = 0
    ndcg5_bert = 0
    turns = np.zeros(n_turns)
    for topic in topics:
        topic_ndcg5s = np.zeros(n_turns)
        topic_ndcg5s[:len(topic.ndcg5_lmd)] = topic.ndcg5_lmd[:n_turns]
        ndcg5_lmd += topic_ndcg5s
        topic_ndcg5s[:len(topic.ndcg5_bert)] = topic.ndcg5_bert[:n_turns]
        ndcg5_bert += topic_ndcg5s
        turns[:len(topic.ndcg5_lmd)] += 1

    ndcg5_lmd = (ndcg5_lmd / len(turns))
    ndcg5_bert = (ndcg5_bert / len(turns))
    plt.figure(frameon=False)
    plt.plot(range(1, n_turns+1), ndcg5_lmd, color="blue", label = 'Elastic Search')
    plt.plot(range(1, n_turns+1), ndcg5_bert, color="red", label = 'Bert')
    plt.legend(loc="upper right")
    plt.xlabel("NDGC@5")
    plt.grid()
    plt.savefig("NDGC@5")
    plt.show()
    plt.close()
    


#plot pr

def plot_precision_recall_per_topic(topic_name, n_turns):
    recall_11point = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    count = 0
    precision_11point_lmd = np.zeros(len(recall_11point))
    precision_11point_bert = np.zeros(len(recall_11point))
    topic = find_topic_name(topic_name)
    if len(topic.recall_var_lmd):
        for i in range(min(len(topic.recall_var_lmd), n_turns)):
            if len(topic.recall_var_lmd[i]):
                precision_11point_lmd_ = np.interp(recall_11point, topic.recall_var_lmd[i], topic.precision_var_lmd[i])
                precision_11point_bert_ = np.interp(recall_11point, topic.recall_var_bert[i], topic.precision_var_bert[i])
                precision_11point_lmd =  np.add(precision_11point_lmd, precision_11point_lmd_)
                precision_11point_bert = np.add(precision_11point_bert, precision_11point_bert_)
                count += 1
    precision_11point_lmd = precision_11point_lmd / count
    precision_11point_bert = precision_11point_bert / count
    
    plt.figure(frameon=False)
    plt.plot(recall_11point, np.flip(np.maximum.accumulate(np.flip(precision_11point_lmd))), color='blue', label='Elastic Search')
    plt.plot(recall_11point, np.flip(np.maximum.accumulate(np.flip(precision_11point_bert))), color='red', label='Bert')
    plt.legend(loc="upper right")
    plt.xlabel("Precision-Recall topic " + str(topic_name))
    plt.grid()
    plt.savefig("Precision-Recall topic " + str(topic_name))
    plt.show()
    plt.close()


def plot_precision_recall_per_topic_turn(topic_name, n_turns):
    recall_11point = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    precision_11point_lmd = np.zeros(len(recall_11point))
    precision_11point_bert = np.zeros(len(recall_11point))
    topic = find_topic_name(topic_name)
    if len(topic.recall_var_lmd):
         for i in range(min(len(topic.recall_var_lmd), n_turns)):
            if len(topic.recall_var_lmd[i]):
                precision_11point_lmd = np.interp(recall_11point, topic.recall_var_lmd[i], topic.precision_var_lmd[i])
                precision_11point_bert = np.interp(recall_11point, topic.recall_var_bert[i], topic.precision_var_bert[i])
                plt.figure(frameon=False)
                plt.plot(recall_11point, np.flip(np.maximum.accumulate(np.flip(precision_11point_lmd))), color="blue", label = 'Elastic Search')
                plt.plot(recall_11point, np.flip(np.maximum.accumulate(np.flip(precision_11point_bert))), color="red", label = 'Bert')
                plt.legend(loc="upper right")
                plt.xlabel("Precision-Recall topic" + str(topic_name) + " turn " + str(i+1))
                plt.grid()
                plt.savefig("Precision-Recall topic" + str(topic_name) + " turn " + str(i+1))
                plt.show()
                plt.close()

def plot_precision_recall_per_turn(n_turns):
    recall_11point = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    for i in range(n_turns):
        count = 0
        precision_11point_lmd = np.zeros(len(recall_11point))
        precision_11point_bert = np.zeros(len(recall_11point))
        for topic in topics:
            if i < len(topic.recall_var_lmd) and len(topic.recall_var_lmd[i]):
                precision_11point_lmd = np.add(precision_11point_lmd , np.interp(recall_11point, topic.recall_var_lmd[i], topic.precision_var_lmd[i]))
                precision_11point_bert = np.add(precision_11point_bert, np.interp(recall_11point, topic.recall_var_bert[i], topic.precision_var_bert[i]))
                count += 1
        precision_11point_lmd = precision_11point_lmd / count
        precision_11point_bert = precision_11point_bert / count
        plt.figure(frameon=False)
        plt.plot(recall_11point, np.flip(np.maximum.accumulate(np.flip(precision_11point_lmd))), color='blue', label = 'Elastic Search')
        plt.plot(recall_11point, np.flip(np.maximum.accumulate(np.flip(precision_11point_bert))), color='red', label = 'Bert')
        plt.legend(loc="upper right")
        plt.xlabel("Average Precision-Recall turn " + str(i+1))
        plt.grid()
        plt.savefig("Average Precision-Recall turn " + str(i+1))
        plt.show()
        plt.close()