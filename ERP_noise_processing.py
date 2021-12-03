import matplotlib.pyplot as plt
import numpy as np

class EP_data:
    
    def __init__(self,name): # 파일명 변수 지정 
        self.name=name

    def load_data(self): # 파일 읽기
        f=open(self.name,'r')
        lines=f.readlines()
        data=[]
        for i in lines:
            eeg=float(i)
            data.append(eeg)
        f.close()
        return data
    
    def data_split(self): # 데이터 파싱
        sum_,number=[0]*512,0
        data=EP_data.load_data(self)
        for i in range(256,len(data)-256,512):
            pre_list=data[i-256:i+256]; number+=1
            sum_=[sum_[i]+pre_list[i] for i in range(len(sum_))]
        sum_=[sum_[i]/number for i in range(len(sum_))]
        return sum_
    
    def time_shift(self): # 시간 축으로 바꾸기 
        total_data=EP_data.load_data(self)
        avg_data=EP_data.data_split(self)
        total_time=np.linspace(0,int(len(total_data)/256),len(total_data))
        avg_time=np.linspace(-1,1,len(avg_data))
        return total_time,avg_time
        
    def show_result(self): # 그래프 그리기
        total_time,avg_time=EP_data.time_shift(self)
        plt.figure(figsize=(10,5))
        plt.subplot(2,1,1)
        plt.plot(total_time,EP_data.load_data(self),'b')
        plt.title('All of ERP data'); plt.ylabel('ERP(mV)'); plt.xlabel('time(s)')
        plt.subplot(2,1,2)
        plt.plot(avg_time,EP_data.data_split(self),'b')
        plt.title('Average of ERP data'); plt.ylabel('Average ERP(mV)'); plt.xlabel('time(s)')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    f= EP_data('EP_data_2.txt').show_result() # 파일명 입력 
