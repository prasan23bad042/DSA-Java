class Solution {
    static int inversionCount(int arr[]) {
        int n = arr.length;
        int[] t = new int[n];
        return ms(arr, t, 0, n - 1);
    }

    static int ms(int[] a, int[] t, int l, int r) {
        int c = 0;
        if (l < r) {
            int m = (l + r) / 2;
            c += ms(a, t, l, m);
            c += ms(a, t, m + 1, r);
            c += mg(a, t, l, m, r);
        }
        return c;
    }

    static int mg(int[] a, int[] t, int l, int m, int r) {
        int i = l, j = m + 1, k = l;
        int c = 0;

        while (i <= m && j <= r) {
            if (a[i] <= a[j]) {
                t[k++] = a[i++];
            } else {
                t[k++] = a[j++];
                c += (m - i + 1);
            }
        }

        while (i <= m) t[k++] = a[i++];
        while (j <= r) t[k++] = a[j++];

        for (i = l; i <= r; i++) a[i] = t[i];

        return c;
    }
}
