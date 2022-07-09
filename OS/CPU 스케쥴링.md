# CPU 스케쥴링
## CPU 스케쥴링
* 멀티 프로그래밍 시스템에서 필수
* Ready 상태 프로세스 중에서 CPU에 할당할 프로세스를 선택하는 것
* FIFO Queue, Priority Queue 

## 선점형 vs 비선점형
### 비 선점형
* CPU에 선점된 프로세스를 다른 프로세스가 쫓아낼 수 없음
### 선점형
* CPU에 선점된 프로세스를 다른 프로세스가 쫓아낼 수 있음

## Dispatcher
* 컨텍스트 스위칭
* 유저 모드 변경
* 스케줄러가 프로세스를 선택하고 실제 스위칭은 디스패쳐가 함
* `Dispatcher latency`: 프로세스를 교체하는데 걸리는 시간

## 스케쥴링 목표
* CPU utilization: CPU의 효율 극대화
* Throughput: 단위 시간내에 프로세스의 성공 횟수를 높이자
* Turnaround time: CPU 시작부터 프로세스의 종료까지의 시간을 최소화
* **Waiting time**: 프로세스의 ready queue의 대기 시간을 최소화 하자
* Response time: 응답 시간을 최대한 빠르게

## 스케쥴링 해결법
* FCFS: First-Come, First-Served
* SJF: Shortest Job First (SRTF: Shortest Remaining Time First)
* RR: Round-Robin
* Priority-based
* MLQ: Multi-Level Queue
* MLFQ: Multi-Level Feedback Queue

## FCFS
* CPU를 먼저 요청한 프로세스가 먼저 선점
* FIFO queue로 간단 구현 가능
* waiting time의 평균이 비효율적
* 비선점형 스케쥴링
* Convoy Effect(호송 효과)
    * 실행시간이 긴 프로세스 때문에 실행시간이 짧은 프로세스들이 block 되는 현상

## SJF
* 실행시간(Burst Time)이 짧은 프로세스 먼저 선점