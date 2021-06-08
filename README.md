# Hadoop-The-Definitive-Guide
Hadoop Configuration, Hadoop Management and Hadoop Ecosystem

## Contents
1. [Using](#using)
2. [Hadoop Configuration](#hadoop-configuration)
3. [Hadoop Management Tools](#hadoop-management-tools)

----------------------------------------------------------------

## Using
1. **OS** - Ubuntu 20.04.1 LTS (VMware)
2. **BackEnd** - Java (JDK 1.8), **Hadoop(v3.3.0)**

----------------------------------------------------------------

## Hadoop Configuration
1. hadoop Configuration File (하둡 기본 디렉터리 아래의 etc/hadoop/디렉터리 에 존재)
    1. hadoop-env.sh (Bash 스크립트)
        - 하둡을 구성하는 스크립트에서 사용되는 환경변수
    2. mapred-env.sh (Bash 스크립트)
        - 맵리듀스를 구동하는 스크립트에서 사용되는 환경변수 (hadoop-env.sh에서 재정의)
    3. yarn-env.sh (Bash 스크립트)
        - YARN을 구도하는 스크립트에서 사용되는 환경변수 (hadoop-env.sh에서 재정의)
    4. core-site.xml (하둡 설정 XML)
        - HDFS, 맵리듀스, YARN에서 공통적으로 사용되는 I/O 설정과 같은 하둡 코어를 위한 환경 설정 구성
    5. hdfs-site.xml (하둡 설정 XML)
        - 네임노드, 보조 네임노드, 데이터노드 등과 같은 HDFS 데몬을 위한 환경 설정 구성
    6. mapred-site.xml (하둡 설정 XML)
        - 잡 히스토리 서버 같은 맵리듀스 데몬을 위한 환경 설정 구성
    7. yarn-site.xml (하둡 설정 XML)
        - 리소스 매니저, 웹 애플리케이션 프록시 서버, 노드 매니저와 같은 YARN 데몬을 위한 환경 설정 구성
    8. slaves (일반 텍스트)
        - 데이터노드와 노드 매니저를 구동할 컴퓨터의 목록 (행당 하나)
    9. hadoop-metrics2.properties (자바 속성)
        - 메트릭의 표시를 제어하기 위한 속성
    10. log4j.properties (자바 속성)
        - 시스템 로그, 네임노드 감사 로그, JVM 프로세스의 작업 로그
    11. hadoop-policy.xml (하둡 설정 XML)
        - 하둡을 보안 모드로 구동할 때 사용되는 접근제어 목록에 대한 환경 설정 구성
2. Basic configuration
    1. core-site.xml [Default](https://hadoop.apache.org/docs/r3.3.0/hadoop-project-dist/hadoop-common/core-default.xml)
        ```xml
        <?xml version="1.0"?>
        <configuration>
                <property>
                        <name>fs.defaultFS</name>
                        <value>hdfs://namenode/</value>
                </property>
        </configuration>
        ```
    2. hdfs-site.xml [Default](https://hadoop.apache.org/docs/r3.3.0/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
        ```xml
        <?xml version="1.0"?>
        <configuration>
                <property>
                        <name>dfs.namenode.name.dir</name>
                        <value>/disk1/hdfs/name,/remote/hdfs/name</value>
                </property>
                <property>
                        <name>dfs.datanode.data.dir</name>
                        <value>/disk1/hdfs/data,/disk2/hdfs/data</value>
                </property>
                <property>
                        <name>dfs.namenode.checkpoint.dir</name>
                        <value>/disk1/hdfs/namesecondary,/disk2/hdfs/namesecondary</value>
                </property>
        </configuration>
        ```
    3. yarn-site.xml [Default](https://hadoop.apache.org/docs/r3.3.0/hadoop-yarn/hadoop-yarn-common/yarn-default.xml)
        ```xml
        <?xml version="1.0"?>
        <configuration>
                <property>
                        <name>yarn.resourcemanager.hostname</name>
                        <value>resourcemanager</value>
                </property>
                <property>
                        <name>yarn.nodemanager.local-dirs</name>
                        <value>/disk1/nm-local-dir,/disk2/nm-local-dir</value>
                </property>
                <property>
                        <name>yarn.nodemanager.aux-services</name>
                        <value>mapreduce.shuffle</value>
                </property>
                <property>
                        <name>yarn.nodemanager.resource.cpu-vcores</name>
                        <value>16</value>
                </property>
        </configuration>
        ```
    4. hdfs-rbf-site.xml [Default](https://hadoop.apache.org/docs/r3.3.0/hadoop-project-dist/hadoop-hdfs-rbf/hdfs-rbf-default.xml)
    5. mapred-site.xml [Default](https://hadoop.apache.org/docs/r3.3.0/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml)
3. 주요 HDFS 데몬 속성 (core-site.xml, hdfs-site.xml 에서 설정)
    1. fs.defaultFS
        - URI, 기본값 file:///
        - 기본 파일시스템. URI는 호스트명과 네임노드의 RPC 서버가 실행되는 포트 번호를 정의한다. 기본 포트 번호는 8020이다.
    2. dfs.namenode.name.dir
        - 콤마로 구분된 디렉터리 이름, 기본값 file://${hadoop.tmp.dir}/dfs/name
        - 네임노드가 영속적인 메타데이터를 저장할 디렉터리 목록을 지정한다. 네임노드는 메타데이터의 복제본을 목록에 디렉터리별로 저장한다.
    3. dfs.datanode.data.dir
        - 콤마로 구분된 디렉터리 이름, 기본값 file://${hadoop.tmp.dir}/dfs/data
        - 데이터노드가 블록을 저장할 디렉터리 목록. 각 블록은 이 디렉터리 중 오직 한 곳에만 저장된다.
    4. dfs.namenode.checkpoint.dir
        - 콤마로 구분된 디렉터리 이름, 기본값 file://${hadoop.tmp.dir}/dfs/namesecondary
        - 보조 네임노드가 체크포인트를 저장하는 디렉터리 목록. 목록에 있는 각 디렉터리에 체크포인트의 복제본을 저장한다.
    5. hadoop.tmp.dir
        - HDFS의 저장 디렉터리는 별도로 지정하지 않으면 하둡의 임시 디렉터리 하위에 위치한다.
        - hadoop.tmp.dir 속성으로 지정하며 기본값은 /tmp/hadoop-${user.name}
4. 주요 YARN 데몬 속성 (yarn-site.xml 에서 설정)
    1. yarn.resourcemanager.hostname
        - 호스트명, 기본값 0.0.0.0
        - 리소스 매니저가 수행된 머신의 호스트명. 아래에 ${y.rm.hostname} 축약형으로 표기
    2. yarn.resourcemanager.address
        - 호스트명과 포트, 기본값 ${y.rm.hostname}:8032
        - 리소스 매니저의 RPC 서버가 동작하는 호스트명과 포트
    3. yarn.nodemanager.local-dirs
        - 콤마로 구분된 디렉터리명, 기본값 ${hadoop.tmp.dir}/nm-local-dir
        - 컨테이너가 임시데이터를 저장하도록 노드매니저가 정한 디렉터리 목록. 애플리케이션이 종료되면 데이터가 지워진다.
    4. yarn.nodemanager.aux-services
        - 콤마로 구분된 서비스명
        - 노드 매니저가 수행하는 보조 서비스 목록. 서비스는 yarn.nodemanager.aux-services.service-name.class 속성으로 정의된 클래스로 구현된다. 기본적으로 보조 서비스는 지정되지 않는다.
    5. yarn.nodemanager.resource.memory-mb
        - int, 기본값 8192
        - 노드 매니저가 수행할 컨테이너에 할당되는 물리 메모리양(MB 단위)
    6. yarn.nodemanager.vmem-pmem-ratio
        - float, 기본값 2.1
        - 컨테이너에 대한 가상/물리 메모리 비율. 가상 메모리 사용량은 이 비율에 따라 초과 할당될 수 있다.
    7. yarn.nodemanager.resource.cpu-vcores
        - int, 기본값 8
        - 노드 매니저가 컨테이너에 할당할 수 있는 CPU 코어의 수
5. 맵리듀스 잡의 메모리 속성 (클라이언트에서 설정)
    1. mapreduce.map.memory.mb
        - int, 기본값 1024
        - 맵 컨테이너의 메모리 총량
    2. mapreduce.reduce.memory.mb
        - int, 기본값 1024
        - 리듀스 컨테이너의 메모리 총량
    3. mapreduce.child.java.opts
        - String, 기본값 -Xmx200m
        - 맵과 리듀스 태스크를 실행하는 컨테이너 프로세스를 시작하는 데 사용되는 JVM 옵션. 이 속성은 메모리 설정 외에도 디버깅 목적의 JVM 속성을 포함할 수 있다.
    4. mapreduce.map.java.opts
        - String, 기본값 -Xmx200m
        - 맵 테스크를 실행하는 자식 프로세스에서 사용되는 JVM 옵션
    5. mapreduce.reduce.java.opts
        - String, 기본값 -Xmx200m
        - 리듀스 테스크를 실행하는 자식 프로세스에서 사용되는 JVM 옵션
6. 맵 측면에서 튜닝 속성
    1. mapreduce.task.io.sort.mb
        - int, 기본값 100
        - 맵 출력을 정렬하는 동안 사용할 메모리 버퍼의 크기로, 메가바이트 단위
    2. mapreduce.map.sort.spill.percent
        - float, 기본값 0.80
        - 디스크로의 스필을 시작하기 위한 맵 출력 메모리 버퍼와 레코드 경계 인덱스의 한계 사용 비율
    3. mapreduce.task.io.sort.factor
        - int, 기본값 10
        - 파일 정렬 시 한번에 병합할 스트림의 최대 수. 이 속성은 리듀스에서도 사용된다. 100으로 증가시키는 것이 꽤 일반적이다.
    4. mapreduce.map.combine.minspills
        - int, 기본값 3
        - 컴바이너를 실행하기 위해 필요한 스필 파일의 최소 수 (컴바이너가 명시되어 있을 때)
    5. mapreduce.map.output.compress
        - boolean, 기본값 false
        - 맵 출력 압축 여부
    6. mapreduce.map.output.compress.codec
        - Class, 기본값 org.apache.hadoop.io.compress.DefaultCodec
        - 맵 출력에 사용할 압축 코덱
    7. mapreduce.shuffle.max.threads
        - int, 기본값 0
        - 맵 출력을 리듀서에 제공하기 위한 노드 매니저별 워커 스레드 수. 클러스터 전체 설정이며 개별 잡에 설정이 불가능하다. 0은 네티 (Netty) 기본값인 가용 프로세서 수의 두 배다.
7. 리듀스 측면에서 튜닝 속성
    1. mapreduce.reduce.shuffle.parallelcopies
        - int, 기본값 5
        - 맵 출력을 리듀서에 복사하기 위해 사용되는 스레드 수
    2. mapreduce.reduce.shuffle.maxfetchfailures
        - int, 기본값 10
        - 리듀서가 에러를 보고하기 전에 수해하는 맵 출력 인출 시도 수
    3. mapreduce.task.io.sort.factor
        - int, 기본값 10
        - 파일을 정렬할 때 한번에 병합하는 스트림의 최대 수. 이 속성은 맵에서도 사용된다.
    4. mapreduce.reduce.shuffle.input.buffer.percent
        - float, 기본값 0.70
        - 셔플의 복사 단계 동안 맵 출력 버퍼에 할당되는 전체 힙 크기 비율
    5. mapreduce.reduce.shuffle.merge.percent
        - float, 기본값 0.66
        - 출력의 병합과 디스크에 스필을 시작하기 위한 맵 출력 버퍼의 한계 사용 비율
    6. mapreduce.reduce.merge.inmem.threshold0
        - int, 기본값 1000
        - 출력의 병합과 디스크에 스필하는 과정을 시작하기 위한 맵 출력의 한계 수. 0 이하의 값은 한계가 없다는 의미며, 스필 동작은 mapreduce.reduce.shuffle.merge.percent에 의해 결정된다.
    7. mapreduce.reduce.input.buffer.percent
        - float, 기본값 0.0
        - 리듀서가 진행되는 동안 맵 출력을 메모리에 유지하는 데 사용되는 전체 힙 크기의 비율. 리듀스 단계가 시작되면 메모리의 맵 출력 크기는 이 크기를 넘을 수 없다. 기본적으로 리듀스에 가능한 한 많은 메모리를 할당하기 위해 리듀스를 시작하기 전에 모든 맵 출력을 디스크에 병합해놓는다. 하지만 리듀서가 요구하는 메모리가 적다면 디스크 IO를 최소화하기 위해 이 값은 증가될 수 있다.
8. RPC 서버 속성
    1. fs.default.FS
        - 기본값 file:///
        - HDFS URI 설정 시 이 속성은 네임노드의 RPC 서버의 주소와 포트를 정의한다. 지정하지 않으면 기본 포트는 8020이다.
    2. dfs.namenode.rpc-bind-host
        - 네임노드의 RPC 서버가 바인드할 주소. 설정하지 않으면 바인드 주소는 fs.defaultFS 속성의 값으로 정의된다. 0.0.0.0 으로 설정하면 네임노드가 모든 인터페이스에 대해 대기하도록 할 수 있다.
    3. dfs.datanode.ipc.address
        - 기본값 0.0.0.0:50020
        - 데이터노드의 RPC 서버 주소와 포트
    4. mapreduce.jobhistory.address
        - 기본값 0.0.0.0:10020
        - 잡 히스토리 서버의 RPC 서버 주소와 포트. 이 속성은 클라이언트 (일반적으로 클러스터 외부)가 잡 히스토리를 쿼리하기 위해 사용한다.
    5. mapreduce.jobhistory.bind-host
        - 잡 히스토리 서버의 RPC와 HTTP 서버가 바인드할 주소
    6. yarn.resourcemanager.hostname
        - 기본값 0.0.0.0
        - 리소스 매니저가 수행될 머신의 호스트명. 아래에 ${y.rm.hostname} 축약형으로 표기
    7. yarn.resourcemanager.bind-host
        - 리소스 매니저의 RPC와 HTTP 서버가 바인드하는 주소
    8. yarn.resourcemanager.address
        - 기본값 ${y.rm.hostname}:8032
        - 리소스 매니저의 RPC 서버 주소와 포트. 이 속성은 클라이언트 (일반적으로 클러스터 외부)가 리소스 매니저와 통신하기 위해 사용한다.
    9. yarn.resourcemanager.admin.address
        - 기본값 ${y.rm.hostname}:8033
        - 리소스 매니저의 admin RPC 서버 주소와 포트. admin 클라이언트 (일반적으로 클러스터 외부에서 yarnadmin으로 수행)가 리소스 매니저와 통신하기 위해 사용한다.
    10. yarn.resourcemanager.scheduler.address
        - 기본값 ${y.rm.hostname}:8030
        - 리소스 매니저 스케줄러의 RPC 서버의 주소와 포트. 이 속성은 클러스터 내 애플리케이션 마스터가 리소스 매니저와 통신하기 위해 사용한다.
    11. yarn.resourcemanager.resource-tracker.address
        - 기본값 ${y.rm.hostname}:8031
        - 리소스 매니저 리소스 트래커의 RPC 서버 주소 및 포트. 이 속성은 클러스터 내 노드 매너지가 리소스 매니저와 통신하기 위해 사용한다.
    12. yarn.nodemanager.hostname
        - 기본값 0.0.0.0
        - 노드 매니저가 수행되는 머신의 호스트명. 아래에 ${y.nm.hostname} 축약형으로 표기
    13. yarn.nodemanager.bind-host
        - 노드 매너지의 RPC와 HTTP 서버가 바인드할 주소
    14. yarn.nodemanager.address
        - 기본값 ${y.nm.hostname}:0
        - 노드 매너지의 RPC 서버 주소와 포트. 이 속성은 클러스터 내 애플리케이션 마스터가 노드 매너지와 통신하기 위해 사용한다.
    15. yarn.nodemanager.localizer.address
        - 기본값 ${y.nm.hostname}:8040
        - 노드 매니저 로컬라이저의 RPC 서버 주소와 포트
9. HTTP 서버 속성
    1. dfs.namenode.http-address
        - 기본값 0.0.0.0:50070
        - 네임노드의 HTTP 서버 주소와 포트
    2. dfs.namenode.http-bind-host
        - 네임노드의 HTTP 서버가 바인드할 주소
    3. dfs.namenode.secondary.http-address
        - 기본값 0.0.0.0:50090
        - 보조 네임노드의 HTTP 서버 주소와 포트
    4. dfs.datanode.http.address
        - 기본값 0.0.0.0:50075
        - 데이터노드의 HTTP 서버 주소와 포트.
    5. mapreduce.jobhistory.webapp.address
        - 기본값 0.0.0.0:19888
        - 맵리듀스 잡 히스토리 서버의 주소와 포트. 이 속성은 mapred-site.xml에서 설정한다.
    6. mapreduce.shuffle.port
        - 기본값  13562
        - 셔플 핸들러의 HTTP 포트 번호. 이 속성은 맵 출력을 처리하는 데 사용되며 웹 UI로 사용자가 접근할 수 없다. 이 속성은 mapred-site.xml에서 설정한다.
    7. yarn.resourcemanager.webapp.address
        - 기본값 ${y.rm.hostname}:8088
        - 리소스 매니저의 HTTP 서버 주소 및 포트
    8. yarn.nodemanager.webapp.address
        - 기본값 ${y.nm.hostname}:8042
        - 노드 매니저의 HTTP 서버 주소 및 포트
    9. yarn.web-proxy.address
        - 웹 애플리케이션 프록시 서버의 HTTP 서버 주소와 포트. 설정하지 않으면 기본으로 웹 애플리케이션 프록시 서버가 리소스 매니저 프로세스 내에서 수행된다.
---------------------------------------------------------------

## Hadoop Management Tools
1. dfsadmin
    - HDFS의 상태 정보를 확인하고 HDFS에서 다양한 관리 작업을 수행할 수 있는 다목적 도구
    - 슈퍼유저 권한이 필요하며, hdfs dfsadmin 명령으로 실행
    - dfsadmin 명령
        1. -help : 입력받은 명령어에 대한 도움말을 보여준다. 명령어를 지정하지 않으면 모든 명령어를 표시한다.
        2. -report : 파일시스템 통계 (웹 UI와 유사)와 연결된 데이터노드 정보를 보여준다.
        3. -metasave : 연결된 데이터노드 리스트와 복제되거나 삭제된 블록 정보를 하둡 로그 디렉터리 내에 파일로 저장한다.
        4. -savemode : 안전 모드의 상태를 변경하거나 조회한다.
        5. -saveNameSpace : 현재 메모리상에 있는 파일시스템 이미지를 새로운 fsimage 파일에 저장하고 edits 파일을 초기화한다. 이 동작은 안전 모드에서만 수행 가능하다.
        6. -fetchImage : 네임노드에서 가장 최신의 fsimage를 찾아 로컬 파일로 저장한다.
        7. -refreshNodes : 네임노드에 접속이 허가된 데이터노드 집합을 갱신한다.
        8. -upgradeProgress : HDFS 업그레이드 진행에 대한 정보를 가져오거나 업그레이드를 강제로 진행한다.
        9. -finalizeUpgrade : 이전 버전의 네임노드와 데이터노드 저장 디렉터리를 제거한다. 업그레이드가 적용되고 새로운 버전으로 클러스터가 성공적으로 실행된 후에 사용할 수 있다.
        10. -setQuota : 디렉터리 할당량을 설정한다. 디렉터리 할당량은 디렉터리 트리 내의 파일과 디렉터리 이름의 개수를 제한한다. 디렉터리 할당량은 사용자가 많은 수의 작은 파일을 생성하는 것을 방지하는 데 유용하며, 네임노드의 메로리를 유지하는 데 도움이 된다.
        11. -clrQuota : 저장된 디렉터리 할당량을 지운다.
        12. -setSpaceQuota : 디렉터리에 용량기준 할당량을 설정한다. 이는 디렉터리 트리 내에 저장할 수 있는 파일의 크기를 제한한다. 사용자에게 제한된 용량의 저장 공간을 제공하는 데 유용하다.
        13. -clrSpaceQuota : 디렉터리에 지정된 용량기준 할당량을 지운다.
        14. -refreshServiceAcl : 네임노드의 서비스 수준 인가 정책 파일을 갱신한다.
        15. -allowSnapshot : 지정된 디렉터리에 스냅숏을 생성하는 것을 허락한다.
        16. -disallowSnapshot : 지정된 디렉터리에 스냅숏을 생성하는 것을 불허한다.
2. fsck
    - HDFS에 저장된 파일의 상태 점검을 위한 유틸리티
    - 적게 혹은 많이 복제된 블록뿐만 아니라 모든 데이터노드에서 사라진 블록을 찾을 수 있다.
    - 입력받은 경로를 시작으로 파일시스템 네임스페이스를 재귀적으로 순회하면서 찾은 파일들을 점검한다.
    - 실행 명령어
        ```bash
        % hdfs fsck <fs path>
        ```
        <p align="center">
            <img src = "Images/fsck.png", width="100%">
        </p>
    - 확인 해야할 상태
        1. 초과 복제 블록 (Over-replicated-blocks) : 이는 파일을 구성하는 블록 중에서 목표 복제 개수를 초과하는 블록이다. 일반적으로 초과 복제는 문제가 되지 않는다. 그리고 HDFS는 초과 블록 복제본을 자동으로 삭제한다.
        2. 복제 기준 미만의 블록 (Under-replicated-blocks) : 이는 파일을 구성하는 블록 중에서 목표 복제 개수에 미치지 못하는 블록으로, HDFS는 목표 복제 개수가 될 때까지 복제 기준에 미달하는 블록의 새로운 복제본을 자동으로 생성한다. hdfs dfsadmin -metasave 명령을 이용하면 복제가 되고 있거나 대기 상태에 있는 블록 정보를 확인할 수 있다.
        3. 잘못 복제된 블록 (Mis-replicated-blocks) : 이는 블록 복제 배치 정책을 만족하지 않는 블록이다. 예를 들어 복제 수준이 3인 멀티랙 클러스터에서 3개의 복제본 모두가 동일한 랙에 있다면 해당 블록은 잘못 복제된 블록이 된다. 복제본이 장애 복구 능력을 갖기 위해서는 최소 2개의 랙에 분산되어 있어야 한다. HDFS는 잘못 복제된 블록을 자동으로 다시 복제하여 랙 배치 정책을 준수하게 만든다.
        4. 손상된 블록 (Corrupt blocks) : 모든 복제본을 사용할 수 없으면 손상된 블록이다. 적어도 한 개의 정상적인 복제본을 가진 블록은 손상된 것으로 보고되지 않는다. 네임노드는 손상되지 않은 블록을 목표 복제 개수에 도달할 때까지 복제한다.
        5. 누락된 복제본 (Missing replicas) : 누락된 블록은 클러스터 어디에서도 복제본을 찾을 수 없는 블록이다.
3. block scanner
    - 모든 데이터노드는 블록 스캐너를 실행하여 데이터노드에 저장된 모든 블록을 주기적으로 점검한다. 이를 통해 클라이언트가 블록을 읽기 전에 문제가 있는 블록을 탐지하고 수리할 수 있다. 블록 스캐너는 점검할 블록의 목록을 관리하며 체크섬 오류를 찾기 위해 모든 블록을 확인한다. 스캐너는 데이터노드의 디스크 대역폭을 유지하기 위한 조절 메커니즘을 사용한다.
    - 시간이 지남에 따라 발생하는 디스크 오류에 대처하기 위해 3주마다 전체 블록을 점검한다. 검사 주기는 dfs.datanode.scan.period.hours 속성으로 설정하며, 기본값은 504시간이다. 손상된 블록이 있으면 네임노드에 보고한다.
    - 데이터노드의 웹 인터페이스인 http://datanode:50075/blockScannerReport를 방문하면 블록 점검 보고서를 얻을 수 있다.
4. balancer
    - 시간이 지남에 따라 데이터노드 사이의 블록의 분포는 불균형 상태가 될 수 있다. 불균형 상태의 클러스터는 맵리듀스의 지역성에 영향을 받게 되므로 자주 사용되는 데이터노드에 큰 부하를 주게 된다. 따라서 불균현 상태가 되지 않도록 해야 한다.
    - 밸런서 프로그램은 블록을 재분배하기 위해 사용률이 높은 데이터노드의 블록을 사용률이 낮은 데이터노드로 옮기는 하둡 데몬이다. 블록 복제본을 다른 랙에 두어서 데이터 유실을 방지하는 블록 복제본 배치 정책은 그대로 고수한다. 밸런서는 클러스터가 균형 상태가 될 때까지 블록을 이동시킨다. 여기서 균형 상태란 각 데이터노드의 사용률 (노드의 총 가용 공간과 사용된 공간의 비율)이 클러스터의 사용률 (클러스터의 총 가용 공간과 사용된 공간의 비율)과 비교하여 지정된 임계치 비율 이내일 때를 의미한다.
    - 실행 명령어
        ```bash
        % start-balancer.sh
        ```
    - -threshold 인자에는 클러스터의 균형 상태를 의미하는 임계치 비율을 지정한다. 이 플래그는 선택사항이며, 지정하지 않으면 임계치는 10%다. 클러스터에는 오직 하나의 밸런서만 실행될 수 있다.