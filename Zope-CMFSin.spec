%define		zope_subname	CMFSin
Summary:	A Zope product that is a simple syndication client for CMF
Summary(pl):	Dodatek do Zope bêd±cy prostym klientem "korporacyjnym" dla CMF
Name:		Zope-%{zope_subname}
Version:	0.6.1
Release:	7
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}.tar.gz
# Source0-md5:	a50ab5b9c13526a6a52397d556b09e84
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	Zope-CMF
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	CMF

%description
This is a simple syndication client for CMF. It uses rssparser and
shares many things in common with CMFNewsFeed but has a different
model for handling channels. It is designed to map _n_ channels or
feeds to sets of composite virtual channels which can then be called
in in a timely fashion.

%description -l pl
CMFSin jest prostym klientem "korporacyjnym" dla CMF. Umo¿liwia
parsowanie rss i posiada wiele mo¿liwo¶ci jakie daje CMFNewsFeed, lecz
ró¿ni siê innym modelem obs³ugi kana³ów. Jest opracowany tak, by
odwzorowywaæ _n_ kana³ów lub strumieni na zbiory po³±czonych
wirtualnych kana³ów, które mog± byæ wywo³ywane o okre¶lonej porze.

%prep
%setup -q -n %{zope_subname}

find . -type d -name CVS | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,skins,www,*.py,*.cfg,*.gif,version.txt,refresh.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc docs/* README.txt
%{_datadir}/%{name}
