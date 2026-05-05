#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
// TOPIC: Threads (pthreads) | gcc -o out 07_threads.c -lpthread && ./out

int main(void) {
    // TODO 1: Create and join a thread
    //   void *worker(void *arg) {
    //       int id = *(int *)arg;
    //       printf("Thread %d running\n", id);
    //       return NULL;
    //   }
    //   pthread_t t;
    //   int id = 1;
    //   pthread_create(&t, NULL, worker, &id);
    //   pthread_join(t, NULL);

    // TODO 2: Mutex — protect shared state
    //   pthread_mutex_t mu = PTHREAD_MUTEX_INITIALIZER;
    //   int counter = 0;
    //   void *increment(void *arg) {
    //       for (int i = 0; i < 1000; i++) {
    //           pthread_mutex_lock(&mu);
    //           counter++;
    //           pthread_mutex_unlock(&mu);
    //       }
    //       return NULL;
    //   }
    //   // Spawn 10 threads → counter should be 10000

    // TODO 3: Condition variable — producer / consumer
    //   pthread_mutex_t mu  = PTHREAD_MUTEX_INITIALIZER;
    //   pthread_cond_t  cond = PTHREAD_COND_INITIALIZER;
    //   int ready = 0;
    //   // Producer: lock, set ready=1, signal
    //   // Consumer: lock, while (!ready) pthread_cond_wait(&cond, &mu), unlock

    // TODO 4: Thread pool (fixed N workers, shared job queue)
    //   // Use mutex-protected linked list as job queue
    //   // Worker loop: lock → dequeue job → unlock → execute
    //   // Main: enqueue N jobs, signal workers, join all

    // TODO 5: Read-write lock
    //   pthread_rwlock_t rwlock = PTHREAD_RWLOCK_INITIALIZER;
    //   pthread_rwlock_rdlock(&rwlock);   // multiple readers OK
    //   pthread_rwlock_wrlock(&rwlock);   // exclusive writer
    //   pthread_rwlock_unlock(&rwlock);

    // TODO 6: Thread-local storage
    //   __thread int tls_counter = 0;  // each thread has its own copy
    //   // Or POSIX: pthread_key_create, pthread_setspecific, pthread_getspecific

    // TODO 7: Semaphore via POSIX sem_t
    //   #include <semaphore.h>
    //   sem_t sem; sem_init(&sem, 0, 3);  // max 3 concurrent
    //   sem_wait(&sem);                    // acquire
    //   // ... critical section ...
    //   sem_post(&sem);                    // release

    // TODO 8: Spinlock for low-latency critical sections
    //   pthread_spinlock_t spin;
    //   pthread_spin_init(&spin, PTHREAD_PROCESS_PRIVATE);
    //   pthread_spin_lock(&spin);
    //   // ... very short critical section ...
    //   pthread_spin_unlock(&spin);

    printf("TODO: implement thread exercises\n");
    return 0;
}
