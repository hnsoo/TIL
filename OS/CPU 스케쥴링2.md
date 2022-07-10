# CPU 스케쥴링
## SRTF (Preemptive SJF)
* 남아있는 시간이 짧은 프로세스를 먼저 선점
* 선점형 알고리즘

![srtf](https://github.com/hnsoo/TIL/blob/master/assets/srtf.png?raw=true)

## RR (Round Robin)
* 시분할을 이용한 선점형 FCFS
* 일정 시간(`time quantum`) 동안 프로세스가 실행되고 다음 프로세스에게 선점을 넘겨주는 방식
* `원형 큐` 형태의 레디 큐를 순회하면서 프로세스 선점
* `time quantum`의 값을 얼마로 주느냐에 따라 O/S 성능이 결정

## RR 두가지 상황
* `time quantum`보다 실행 시간이 짧을 때
    * 사용이 끝난 프로세스는 CPU를 자진 반납
    * 그 다음 레디 큐에 있는 프로세스 실행
* `time quantum`보다 실행 시간이 길 때
    * OS에 의해 인터럽트가 발생
    * 컨텍스트 스위칭이 일어나고 실행중이던 프로세스는 레디 큐 마지막으로 이동

## 우선순위(Priority-base) 스케쥴링
* 제일 중요한 프로세스를 우선적으로 실행
* 선점형(SRTF), 비선점형(SJF) 둘다 가능
* `starvation`(기아) 문제
    * 낮은 중요도의 프로세스가 레디 큐에서 무한 대기할 수 있음
    * `aging` 도입으로 해결
    * `aging`: 레디큐에 오래 있을 수록 중요도 상승

## RR + 우선순위 스케쥴링
* 높은 우선순위 프로세스를 먼저 실행
* 만약 우선순위가 같을 경우 RR 

![rr-priority](https://github.com/hnsoo/TIL/blob/master/assets/rr-priority.png?raw=true)

## Multi-Level Queue(MLQ)
* 각 우선순위별로 레디 큐를 따로 생성

![mlq](https://github.com/hnsoo/TIL/blob/master/assets/mlq.png?raw=true)

## Multi-Level Feedback Queue(MLFQ)
* 각 레벨에서 프로세스를 끝내지 못하면 다음 레벨로 이동
* 각 레벨이 지날 수록 선점 시간을 길게 주어 CPU burst가 긴 프로세스 또한 다 실행 할 수 있게 함

![mlfq](https://github.com/hnsoo/TIL/blob/master/assets/mlfq.png?raw=true)

## 쓰레드 스케쥴링
* 현대에서는 쓰레드 스케쥴링이 많이 쓰임
* 프로세스 스케쥴링과 쓰레드 스케쥴링 기본 동작 방식을 같음
* 운영체제는 `커널 쓰레드`만 스케줄링
* `유저 쓰레드`는 **쓰레드 라이브러리**가 관리

## Real-Time(실시간) OS
* 주어진 시간내에 작업을 완료하는 OS
* Soft RealTtime vs Hard Realtime

### Soft Realtime
* 매우 중요한 (critical) 프로세스가 반드시 주어진 시간내에 실행되지는 않음
* 그러나 다른 일반적인 프로세스보다는 우선적으로 실행되도록 보장
* 예) 스마트폰 음성 신호 변환

### Hard Realtime
* 어떤 작업이 반드시 주어진 시간 (Deadline)내에 실행
* 예) 우주 탐사선